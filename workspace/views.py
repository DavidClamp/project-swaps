import json
import QuantLib as ql
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Trade, HistoricalRate
from .data_handler import import_bluegamma_data
from .utils import get_sofr_curve, calculate_trade_npv
from .forms import TradeForm

@login_required
def dashboard(request):
    """The main workspace landing page showing Portfolio Summary"""
   # If DB is empty, fill it automatically
    if not HistoricalRate.objects.exists():
        from .data_handler import import_bluegamma_data
        import_bluegamma_data(source="local")
        
    # DEFENSIVE FETCH: .first() returns None instead of crashing if empty
    latest_rate = HistoricalRate.objects.filter(index_name='SOFR').order_by('-date').first()
    
    if latest_rate:
        latest_date = latest_rate.date
    else:
        latest_date = "No Market Data Found - Please Refresh"

    # Calculate Total Portfolio NPV across all trades
    trades = Trade.objects.filter(user=request.user)
    total_npv = sum(t.last_npv for t in trades if t.last_npv) or 0.0
    
    context = {
        'trades': trades,
        'total_npv': total_npv,
        'trade_count': trades.count(),
        'latest_date': latest_date,
    }
    return render(request, 'workspace/dashboard.html', context)

@login_required
def curve_analyser(request):
    """Generates a mathematically bootstrapped Zero Curve for Chart.js"""
    try:
        latest_date = HistoricalRate.objects.latest('date').date
        # 1. Get the Math Engine (QuantLib Curve)
        curve = get_sofr_curve(latest_date)
        
        # 2. Create smooth plot points (1Y, 2Y, 3Y, 5Y, 7Y, 10Y, 20Y, 30Y)
        plot_tenors = ["1Y", "2Y", "3Y", "5Y", "7Y", "10Y", "20Y", "30Y"]
        plot_rates = []
        
        for t in plot_tenors:
            # Convert '5Y' string to numeric years for QuantLib
            years = float(t.replace('Y', ''))
            # Get the bootstrapped Zero Rate (%) at that exact point
            z_rate = curve.zeroRate(years, ql.Continuous).rate() * 100
            plot_rates.append(round(z_rate, 4))

        context = {
            'tenors': json.dumps(plot_tenors),
            'rates': json.dumps(plot_rates),
            'latest_date': latest_date,
        }
    except HistoricalRate.DoesNotExist:
        messages.warning(request, "No market data found. Please refresh BlueGamma data.")
        context = {'tenors': [], 'rates': [], 'latest_date': 'N/A'}

    return render(request, 'workspace/analyser.html', context)

@login_required
def refresh_market_data(request):
    """Triggers the BlueGamma data import and re-prices the blotter"""
    if request.method == "POST":
        result = import_bluegamma_data(source="local")
        
        # Pro Move: Re-price all user trades against the new data
        latest_date = HistoricalRate.objects.latest('date').date
        curve = get_sofr_curve(latest_date)
        trades = Trade.objects.filter(user=request.user)
        
        for trade in trades:
            calculate_trade_npv(trade.id, curve)
            
        messages.success(request, f"{result} and all portfolio trades re-priced.")
    
    return redirect('analyser')

@login_required
def trade_blotter(request):
    """
    Displays the user's saved trades in a table.
    """
    trades = Trade.objects.filter(user=request.user).order_by('-created_at')
    
    context = {
        'trades': trades,
    }
    return render(request, 'workspace/blotter.html', context)

@login_required
def add_trade(request):
    if request.method == "POST":
        form = TradeForm(request.POST)
        if form.is_valid():
            trade = form.save(commit=False)
            trade.user = request.user
            trade.save()
            
            # Immediate Re-pricing
            latest_date = HistoricalRate.objects.latest('date').date
            curve = get_sofr_curve(latest_date)
            calculate_trade_npv(trade.id, curve)
            
            messages.success(request, f"Trade {trade.trade_id} executed and priced.")
            return redirect('blotter')
    else:
        form = TradeForm()
    return render(request, 'workspace/add_trade.html', {'form': form})

from django.shortcuts import get_object_or_404
from .forms import TradeForm

@login_required
def edit_trade(request, pk):
    """
    Update an existing trade ticket. 
    """
    trade = get_object_or_404(Trade, pk=pk, user=request.user)
    
    if request.method == "POST":
        form = TradeForm(request.POST, instance=trade)
        if form.is_valid():
            trade = form.save()
            
            # Re-price immediately so the dashboard stays accurate
            latest_date = HistoricalRate.objects.latest('date').date
            curve = get_sofr_curve(latest_date)
            calculate_trade_npv(trade.id, curve)
            
            messages.success(request, f"Trade {trade.trade_id} updated and re-priced.")
            return redirect('blotter')
    else:
        form = TradeForm(instance=trade)
    
    return render(request, 'workspace/edit_trade.html', {'form': form, 'trade': trade})

@login_required
def delete_trade(request, pk):
    """
    Remove a trade from the blotter.
    """
    trade = get_object_or_404(Trade, pk=pk, user=request.user)
    
    if request.method == "POST":
        trade_id = trade.trade_id
        trade.delete()
        messages.warning(request, f"Trade {trade_id} successfully removed from blotter.")
        return redirect('blotter')
        
    return render(request, 'workspace/delete_confirm.html', {'trade': trade})


@login_required
def dashboard(request):
    """
    Aggregate trades into 'Strategies' or 'Groups'.
    """
    # Fetch the current user's trades
    trades = Trade.objects.filter(user=request.user)
    
    # Strategy gouping 
  
    strategies = {}
    for t in trades:
        # Fallback: If no group_id exists, treat it as a standalone 'Outright'
        gid = t.group_id if t.group_id else f"OUTRIGHT-{t.trade_id}"
        
        # Initialise entry for a new strategy group
        if gid not in strategies:
            strategies[gid] = {
                'npv': 0.0, 
                'count': 0, 
                'strategy': t.strategy,
                'ticker': t.ticker
            }
        
        # Perform the Aggregation-Summing the last_npv for all legs within this group
        strategies[gid]['npv'] += (t.last_npv or 0.0)
        strategies[gid]['count'] += 1

    #  Total Portfolio Metrics
    total_npv = sum(t.last_npv for t in trades if t.last_npv) or 0.0
    
    context = {
        'strategies': strategies,
        'total_npv': total_npv,
        'trade_count': trades.count(),
        'latest_date': HistoricalRate.objects.filter(index_name='SOFR').order_by('-date').first().date
    }
    return render(request, 'workspace/dashboard.html', context)



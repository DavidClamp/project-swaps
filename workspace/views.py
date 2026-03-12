import json
import QuantLib as ql
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Trade, HistoricalRate
from .data_handler import import_bluegamma_data
from .utils import get_sofr_curve, calculate_trade_npv

@login_required
def dashboard(request):
    """The main workspace landing page showing Portfolio Summary"""
     #DEFENSIVE FETCH: .first() returns None instead of crashing if empty
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

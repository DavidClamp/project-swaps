import json
import QuantLib as ql
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from allauth.account.decorators import verified_email_required
from django.core.management import call_command
from datetime import date

# --- MODELS & FORMS ---
from .models import Trade, HistoricalRate
from .forms import TradeForm
from .data_handler import import_bluegamma_data

# --- UTILITIES (Fixed Imports) ---
# Using parentheses allows us to break lines safely without SyntaxErrors
from .utils import (
    get_sofr_curve,
    calculate_trade_npv,
    get_histogram_data,
    get_forward_histogram_data,
    get_forward_term_structure,
)


@login_required
def curve_analyser(request):
    """
    Tool 1: The SPOT CURVE (Line Chart).
    Visualise the 'Basis' between Market Par Rates (Input) and Zero Rates (Output).
    """
    try:
        latest_entry = (
            HistoricalRate.objects.filter(index_name="SOFR")
            .order_by("-date")
            .first()
        )
        if not latest_entry:
            messages.warning(request, "No market data found. Please refresh.")
            return render(
                request, "workspace/analyser.html", {"tenors": [], "rates": []}
            )

        # 1. Maths (QuantLib)
        curve = get_sofr_curve(latest_entry.date)
        curve.enableExtrapolation()

        # 2. Define Tenors to Plot
        plot_tenors = ["1Y", "2Y", "3Y", "5Y", "7Y", "10Y", "20Y", "30Y"]

        # 3. Build the Datasets
        zero_rates = []
        par_rates = []

        for t in plot_tenors:
            years = float(t.replace("Y", ""))

            # A. Calculate Zero Rate (The "Pure" Spot Rate)
            z_rate = curve.zeroRate(years, ql.Continuous).rate() * 100
            zero_rates.append(round(z_rate, 4))

            # B. Market Par Rate (The "Raw" Swap Rate)
            # Fetch the actual tradeable rate from the DB to compare
            try:
                # Note: Ensure your DB stores rates as decimals (0.045). Mult by 100 for display.
                market_obj = HistoricalRate.objects.filter(
                    date=latest_entry.date, tenor=t, index_name="SOFR"
                ).first()

                if market_obj:
                    par_rates.append(round(float(market_obj.rate) * 100, 4))
                else:
                    par_rates.append(None)
            except Exception:
                par_rates.append(None)

        context = {
            "tenors": json.dumps(plot_tenors),
            "zero_rates": json.dumps(zero_rates),
            "par_rates": json.dumps(par_rates),
            "latest_date": latest_entry.date,
        }
        return render(request, "workspace/analyser.html", context)

    except Exception as e:
        messages.error(request, f"Error generating curve: {e}")
        return redirect("dashboard")


@login_required
def refresh_market_data(request):
    """
    1. Attempt Live API Fetch
    2. Fallback to 3,130-line Back-up Data if API fails
    3. Re-price all portfolio trades
    """
    if request.method == "POST":
        try:
            # --- ATTEMPT LIVE API ---
            # This uses your new API Key from env.py
            result = import_bluegamma_data(source="api")
            messages.success(request, f"Live Sync Success: {result}")
        except Exception as e:
            # --- EMERGENCY FALLBACK ---
            # If trial ended or API is down, load the Big Data
            call_command("loaddata", "testing_default.json")
            messages.warning(
                request,
                "API Offline/Expired. Reverted to 3,130-point Back-up Data.",
            )

        # --- RE-VALUE PORTFOLIO ---
        try:
            latest_rate = (
                HistoricalRate.objects.filter(index_name="SOFR")
                .order_by("-date")
                .first()
            )
            if latest_rate:
                curve = get_sofr_curve(latest_rate.date)
                trades = Trade.objects.filter(user=request.user)
                for trade in trades:
                    calculate_trade_npv(trade.id, curve)
                messages.info(
                    request,
                    "Portfolio NPVs re-calculated against latest curve.",
                )
        except Exception as err:
            messages.error(
                request, f"Market Sync OK, but re-pricing failed: {err}"
            )

    return redirect("dashboard")


@login_required
def trade_blotter(request):
    """
    Displays the user's saved trades in a table.
    """
    trades = Trade.objects.filter(user=request.user).order_by("-created_at")

    context = {
        "trades": trades,
    }
    return render(request, "workspace/blotter.html", context)


@login_required
def add_trade(request):
    if request.method == "POST":
        form = TradeForm(request.POST)
        if form.is_valid():
            trade = form.save(commit=False)
            trade.user = request.user
            trade.save()

            # Immediate Re-pricing
            latest_date = HistoricalRate.objects.latest("date").date
            curve = get_sofr_curve(latest_date)
            calculate_trade_npv(trade.id, curve)
            messages.success(
                request, f"Trade {trade.trade_id} executed and priced."
            )
            return redirect("blotter")
    else:
        form = TradeForm()
    return render(request, "workspace/add_trade.html", {"form": form})


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
            latest_date = HistoricalRate.objects.latest("date").date
            curve = get_sofr_curve(latest_date)
            calculate_trade_npv(trade.id, curve)
            messages.success(
                request, f"Trade {trade.trade_id} updated and re-priced."
            )
            return redirect("blotter")
    else:
        form = TradeForm(instance=trade)
    return render(
        request, "workspace/edit_trade.html", {"form": form, "trade": trade}
    )


@login_required
def delete_trade(request, pk):
    """
    Remove a trade from the blotter.
    """
    trade = get_object_or_404(Trade, pk=pk, user=request.user)
    if request.method == "POST":
        trade_id = trade.trade_id
        trade.delete()
        messages.warning(
            request, f"Trade {trade_id} successfully removed from blotter."
        )
        return redirect("blotter")
    return render(request, "workspace/delete_confirm.html", {"trade": trade})


@login_required
def dashboard(request):
    """
    Aggregate trades into 'Strategies' or 'Groups'.
    """
    trades = Trade.objects.filter(user=request.user)
    strategies = {}

    # 1. Grouping Logic
    for t in trades:
        gid = t.group_id if t.group_id else f"OUTRIGHT-{t.trade_id}"
        if gid not in strategies:
            strategies[gid] = {
                "npv": 0.0,
                "count": 0,
                "strategy": t.get_strategy_display(),
                "ticker": t.ticker,
            }
        # Add trade NPV (handle None as 0.0)
        strategies[gid]["npv"] += float(t.last_npv or 0.0)
        strategies[gid]["count"] += 1

    # 2. Calculate Global Totals
    total_npv = sum(t.last_npv for t in trades if t.last_npv) or 0.0
    trade_count = trades.count()

    # 3. Get latest rate date safely
    latest_rate = (
        HistoricalRate.objects.filter(index_name="SOFR")
        .order_by("-date")
        .first()
    )
    latest_date = latest_rate.date if latest_rate else "Data Pending"

    # 4. Build KPI List
    kpi_data = [
        # KPI 1: Portfolio NPV (Red/Green)
        (
            "Portfolio NPV",
            "fa-scale-balanced",
            f"${total_npv:,.0f}",
            "text-success" if total_npv >= 0 else "text-danger",
        ),
        # KPI 2: Active Trades
        ("Active Trades", "fa-file-invoice-dollar", trade_count, "text-dark"),
        # KPI 3: Index Focus
        ("Index Focus", "fa-satellite-dish", "USD SOFR", "text-dark"),
    ]

    # 5. Final Context
    context = {
        "strategies": strategies,
        "total_npv": total_npv,
        "trade_count": trade_count,
        "latest_date": latest_date,
        "kpi_data": kpi_data,
    }
    return render(request, "workspace/dashboard.html", context)


@login_required
def forward_histogram(request):
    """
    Render the 1Y Forward Frequency Distribution with basic Market Stats
    """
    # 1. Fetch labels and counts from our NumPy utility
    labels, counts = get_histogram_data(index_name="SOFR", tenor="1Y")
    # 2. Manual Mean Calculation
    raw_rates = HistoricalRate.objects.filter(
        index_name="SOFR", tenor="1Y"
    ).values_list("rate", flat=True)

    if raw_rates:
        # Average * 100 to show as a percentage
        mean_val = (sum(raw_rates) / len(raw_rates)) * 100
    else:
        mean_val = 0

    context = {
        "hist_labels": json.dumps(labels),
        "hist_counts": json.dumps(counts),
        "mean_val": round(mean_val, 2),
        "sample_size": len(raw_rates),
        "title": "USD SOFR 1Y Forward Distribution",
    }
    return render(request, "workspace/histogram.html", context)


@login_required
def curve_bar_chart(request):
    """Term Structure Snapshot: Finds the latest available curve points."""
    # 1. Get the absolute latest entry in the DB to find the 'Current' market date
    latest_entry = (
        HistoricalRate.objects.filter(index_name="SOFR")
        .order_by("-date")
        .first()
    )
    if not latest_entry:
        return redirect("home")

    # 2. Define the exact Master Order for the X-axis
    order = [
        "1Y",
        "2Y",
        "3Y",
        "4Y",
        "5Y",
        "6Y",
        "7Y",
        "8Y",
        "9Y",
        "10Y",
        "15Y",
        "30Y",
    ]

    # 3. Fetch ALL rates for THAT specific latest date
    rates_qs = HistoricalRate.objects.filter(
        index_name="SOFR", date=latest_entry.date
    )

    # 4. Filter and Sort based on our Master Order
    # This ensures only the tenors we want appear, in the right order
    sorted_data = []
    for tenor in order:
        match = rates_qs.filter(tenor=tenor).first()
        if match:
            sorted_data.append(match)

    plot_labels = [r.tenor for r in sorted_data]
    plot_rates = [round(float(r.rate) * 100, 4) for r in sorted_data]

    context = {
        "labels": json.dumps(plot_labels),
        "rates": json.dumps(plot_rates),
        "title": f"USD SOFR Term Structure ({latest_entry.date})",
        "sample_size": len(plot_labels),
    }
    return render(request, "workspace/curve_bars.html", context)


# Upgrade request


@login_required
def subscription_plans(request):
    """Direct to window to upgrade to Pro."""
    return render(request, "workspace/plans.html")


# Add the Custom Error Handler Views for your Safety Nets
def custom_404(request, exception):
    """Render the branded Safety Net page"""
    return render(request, "404.html", status=404)


def custom_500(request):
    """Render the branded 500 error page"""
    return render(request, "500.html", status=500)


@login_required
def forward_rate_analysis(request):
    # 1. Get forward rates
    labels, counts, size, mean = get_forward_histogram_data(index_name="SOFR")

    # 2. Prepare Context for the Template
    context = {
        # Data for Chart.js
        "hist_labels": labels,
        "hist_counts": counts,
        # Statistics for the "Grid"
        "sample_size": size,
        "mean_val": mean,
        # Titles
        "title": "1Y Forward Rate (1y1y)",
        "sub_title": "Implied 1Y Rate, starting 1 Year from today",
    }

    # 3. Render the "Purple" Template
    return render(request, "workspace/histogram.html", context)


@login_required
def forward_curve_view(request):
    """
    Tool 2: FORWARD TERM STRUCTURE (Bar Chart).
    URL: /term-structure/ (name='curve_bars')
    """
    try:
        # 1. Build Today's Curve
        # Assume the latest date in the DB is the "Analysis Date"
        today_rate = (
            HistoricalRate.objects.filter(index_name="SOFR")
            .order_by("-date")
            .first()
        )

        if not today_rate:
            messages.warning(
                request,
                "No market data found. Please run 'Refresh Market Data'.",
            )
            return redirect("dashboard")

        curve = get_sofr_curve(today_rate.date)

        # 2. Calculate Forward Path
        # If curve is None (build failed), returns [], []
        labels, rates = get_forward_term_structure(curve, max_years=10)

        # --- SAFETY CHECK START ---
        # If the curve failed, rates will be empty.
        if rates:
            current_val = f"{rates[0]:.2f}%"
            terminal_val = f"{rates[-1]:.2f}%"
        else:
            current_val = "0.00%"
            terminal_val = "0.00%"
            messages.warning(
                request, "Insufficient data to bootstrap the forward curve."
            )
        # --- SAFETY CHECK END ---

        context = {
            "labels": json.dumps(labels),
            "rates": json.dumps(rates),
            "current_1y": current_val,
            "terminal_rate": terminal_val,
        }
        return render(request, "workspace/curve_bars.html", context)

    except Exception as e:
        # Catch any other math errors (e.g., QuantLib interpolation failure)
        messages.error(request, f"Calculation Error: {e}")
        return redirect("dashboard")

@verified_email_required
@login_required
def dashboard(request):
    """
    Mandatory terminal gate. Blocks unverified sessions.
    """
    return render(request, 'workspace/dashboard.html')

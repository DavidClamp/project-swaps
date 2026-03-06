from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Trade, HistoricalRate
from .data_handler import import_bluegamma_data

def dashboard(request):
    """The main workspace landing page"""
    return render(request, 'workspace/dashboard.html')

def curve_analyser(request):
    """The curve analyser page"""
    # Get tenors and rates for Chart.js from the latest curve
    latest_rates = HistoricalRate.objects.filter(index_name='SOFR').order_by('date')
    
    context = {
        'tenors': [r.tenor for r in latest_rates],
        'rates': [r.rate for r in latest_rates],
    }
    return render(request, 'workspace/analyser.html', context)

def refresh_market_data(request):
    """Triggers the BlueGamma data import via a button click."""
    if request.method == "POST":
        # Change to "api" when you're ready for the live feed
        result = import_bluegamma_data(source="local") 
        messages.success(request, result)
    
    return redirect('analyser')

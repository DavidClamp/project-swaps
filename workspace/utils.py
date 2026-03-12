import QuantLib as ql
import pandas as pd
import numpy as np
from .models import HistoricalRate, Trade

def can_access_butterfly_analytics(user):
    """
    Check for an active Stripe subscription.
    """
    if not user.is_authenticated:
        return False
    # Returns True if user is staff or has a 'is_subscriber' flag in their Profile
    return getattr(user.profile, 'is_subscriber', False) or user.is_staff

def get_sofr_curve(target_date):
    """
    Bootstrap a Piecewise Log-Linear Discount Curve.
    Convert raw BlueGamma market rates into a zero-coupon yield curve.
    """
    # 1. Fetch historical market rates from Postgres into a Pandas DataFrame
    rates_qs = HistoricalRate.objects.filter(date=target_date, index_name='SOFR')
    if not rates_qs.exists():
        return None
        
    df = pd.DataFrame(list(rates_qs.values('tenor', 'rate')))
    
    # 2. Global QuantLib Settings: Define the evaluation date for bootstrapping
    ql_date = ql.Date(target_date.day, target_date.month, target_date.year)
    ql.Settings.instance().evaluationDate = ql_date
    
    # 3. Build Rate Helpers: Map market tenors (1Y, 5Y, etc.) to SOFR OIS conventions
    helpers = []
    for _, row in df.iterrows():
        helpers.append(ql.SwapRateHelper(
            ql.QuoteHandle(ql.SimpleQuote(row['rate'])),
            ql.Period(row['tenor']), 
            ql.UnitedStates(ql.UnitedStates.Settlement),
            ql.Annual, ql.Unadjusted, ql.Actual360(), ql.Sofr()
        ))
    
    # 4. Bootstrap and return the mathematical YieldTermStructure
    return ql.PiecewiseLogLinearDiscount(
        0,
        ql.UnitedStates(ql.UnitedStates.Settlement),
        helpers, 
        ql.Actual360()
    )

def calculate_trade_npv(trade_id, curve):
    """
    Calculate the Net Present Value (NPV) of a swap.
    """
    if not curve:
        return 0.0

    # 1. Retrieve trade parameters from the database
    trade = Trade.objects.get(id=trade_id)
    notional = float(trade.notional)
    fixed_rate = trade.fixed_rate
    tenor = ql.Period(trade.tenor_years, ql.Years)
    
    # 2. Determine Trade Direction (Payer vs Receiver of the Fixed Leg)
    side = ql.VanillaSwap.Payer if trade.side == 'PAY' else ql.VanillaSwap.Receiver
    
    # 3. Instrument Setup: Standard OIS Swap conventions (Annual Fixed/Floating)
    calendar = ql.UnitedStates(ql.UnitedStates.Settlement)
    curve_handle = ql.RelinkableYieldTermStructureHandle(curve)
    index = ql.Sofr(curve_handle)

    # 4. Generate Payment Schedules using the 'Modified Following' business day convention
    fixed_schedule = ql.Schedule(curve.referenceDate(), 
                                curve.referenceDate() + tenor, 
                                ql.Period(ql.Annual), calendar, 
                                ql.ModifiedFollowing, ql.ModifiedFollowing, 
                                ql.DateGeneration.Forward, False)
    
    floating_schedule = ql.Schedule(curve.referenceDate(), 
                                   curve.referenceDate() + tenor, 
                                   ql.Period(ql.Annual), calendar, 
                                   ql.ModifiedFollowing, ql.ModifiedFollowing, 
                                   ql.DateGeneration.Forward, False)

    # 5. Build the Swap Object and Attach the Discounting Engine
    swap = ql.VanillaSwap(side, notional, fixed_schedule, fixed_rate, ql.Actual360(),
                          floating_schedule, index, 0.0, ql.Actual360())

    swap.setPricingEngine(ql.DiscountingSwapEngine(curve_handle))

    # 6. Final Valuation: Persist the NPV back to the PostgreSQL database for the Blotter view
    npv = swap.NPV()
    trade.last_npv = npv
    trade.save()

    return npv

def get_histogram_data(index_name='SOFR', tenor='1Y', bins=15):
    """
    Groups historical rates into frequency bins.
    """
    # 1. Pull historical rates for the specific index/tenor
    rates = HistoricalRate.objects.filter(
        index_name=index_name, 
        tenor=tenor
    ).values_list('rate', flat=True)
    
    if not rates or len(rates) < 2:
        return [], []

    # 2. Use Numpy to create the histogram (counts per bin and bin edges)
    counts, bin_edges = np.histogram(rates, bins=bins)
    
    # 3. Create labels using the midpoint of each bin (formatted as %)
    labels = []
    for i in range(len(counts)):
        midpoint = (bin_edges[i] + bin_edges[i+1]) / 2
        labels.append(f"{midpoint*100:.2f}%")
        
    return labels, counts.tolist()


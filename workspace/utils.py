import QuantLib as ql
import pandas as pd
from .models import HistoricalRate, Trade

def can_access_butterfly_analytics(user):
    """
    Gating Logic: Checks if the user has an active 
    Stripe subscription via their Profile.
    """
    if not user.is_authenticated:
        return False
    # Returns True if user is staff or has an active subscription
    return getattr(user.profile, 'is_subscriber', False) or user.is_staff

def get_sofr_curve(target_date):
    """
    The 'Hard Maths': Fetches SOFR rates from Postgres, 
    cleans with Pandas, and builds a QuantLib Zero Curve.
    """
    # 1. Fetch from DB into Pandas
    rates_qs = HistoricalRate.objects.filter(date=target_date, index_name='SOFR')
    if not rates_qs.exists():
        return None
        
    df = pd.DataFrame(list(rates_qs.values('tenor', 'rate')))
    
    # 2. QuantLib Setup
    ql_date = ql.Date(target_date.day, target_date.month, target_date.year)
    ql.Settings.instance().evaluationDate = ql_date
    
    # 3. Build Rate Helpers
    helpers = []
    for _, row in df.iterrows():
        helpers.append(ql.SwapRateHelper(
            ql.QuoteHandle(ql.SimpleQuote(row['rate'])),
            ql.Period(row['tenor']), 
            ql.UnitedStates(ql.UnitedStates.Settlement),
            ql.Annual, ql.Unadjusted, ql.Actual360(), ql.Sofr()
        ))
    
    # 4. Return the mathematical curve
    return ql.PiecewiseLogLinearDiscount(
        0, ql.UnitedStates(), helpers, ql.Actual360()
    )

def calculate_trade_npv(trade_id, curve):
    """
    Prices a specific trade against the QuantLib Zero Curve.
    Supports Outrights and individual Butterfly legs.
    """
    if not curve:
        return 0.0

    # 1. Fetch trade from DB
    trade = Trade.objects.get(id=trade_id)
    
    # 2. QuantLib parameters
    notional = float(trade.notional)
    fixed_rate = trade.fixed_rate
    tenor = ql.Period(trade.tenor_years, ql.Years)
    
    # 3. Define the side (Pay vs Receive)
    # If PAY, then pay fixed (negative NPV if rates go down)
    side = ql.VanillaSwap.Payer if trade.side == 'PAY' else ql.VanillaSwap.Receiver
    
    # 4. Create the Swap Instrument
    # Using standard SOFR conventions (Annual Fixed, Annual Floating)
    calendar = ql.UnitedStates(ql.UnitedStates.Settlement)
    settlement_days = 2
    
    # Link to the curve bootstrapped from BlueGamma
    curve_handle = ql.RelinkableYieldTermStructureHandle(curve)
    index = ql.Sofr(curve_handle)

    # Simplified Swap Engine for the Portfolio view
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

    swap = ql.VanillaSwap(side, notional, fixed_schedule, fixed_rate, ql.Actual360(),
                          floating_schedule, index, 0.0, ql.Actual360())

    # 5. Link the Pricing Engine
    engine = ql.DiscountingSwapEngine(curve_handle)
    swap.setPricingEngine(engine)

    # 6. Save the result back to the Blotter
    npv = swap.NPV()
    trade.last_npv = npv
    trade.save()

    return npv

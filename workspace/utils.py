import QuantLib as ql
import pandas as pd
from .models import HistoricalRate

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


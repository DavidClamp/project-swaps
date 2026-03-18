import json
import random
from datetime import datetime, timedelta

def create_gold_source():
    # 3,130 points: 8 tenors * ~390 trading days
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2026, 3, 17)
    tenors = ['1Y', '2Y', '3Y', '5Y', '7Y', '10Y', '20Y', '30Y']
    
    # Base SOFR rates around 4.5%
    base_rates = {'1Y': 0.045, '2Y': 0.044, '3Y': 0.043, '5Y': 0.042, 
                  '7Y': 0.041, '10Y': 0.041, '20Y': 0.042, '30Y': 0.043}
    
    fixture = []
    pk = 1
    current = start_date

    while current <= end_date:
        if current.weekday() < 5:  # Market Days only
            # Add a small random walk to simulate "Market Volatility"
            daily_vol = random.uniform(-0.0001, 0.0001)
            for t in tenors:
                base_rates[t] += daily_vol
                fixture.append({
                    "model": "workspace.historicalrate",
                    "pk": pk,
                    "fields": {
                        "date": current.strftime('%Y-%m-%d'),
                        "index_name": "SOFR",
                        "tenor": t,
                        "rate": round(base_rates[t], 6)
                    }
                })
                pk += 1
        current += timedelta(days=1)

    with open('workspace/fixtures/testing_default.json', 'w') as f:
        json.dump(fixture, f, indent=2)
    print(f"SUCCESS: Generated {pk-1} rows of Golden Source data.")

if __name__ == "__main__":
    create_gold_source()

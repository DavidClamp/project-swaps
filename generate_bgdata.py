import json
import random
from datetime import datetime, timedelta

def create_gold_source():
    # 6,130 points: 12 tenors * ~570 trading days
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2026, 3, 17)
    tenors = ['1Y', '2Y', '3Y', '4Y', '5Y', '6Y', '7Y', '8Y', '9Y', '10Y', '15Y', '30Y']
    
    base_rates = {
        '1Y': 0.045, '2Y': 0.044, '3Y': 0.043, '4Y': 0.0425, 
        '5Y': 0.042, '6Y': 0.0415, '7Y': 0.041, '8Y': 0.041, 
        '9Y': 0.041, '10Y': 0.041, '15Y': 0.042, '30Y': 0.043
    }

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

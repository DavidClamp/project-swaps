import os
import json
import pandas as pd
import requests
from django.conf import settings
from .models import HistoricalRate

def import_bluegamma_data(source="api"):
    """
    Hybrid Data Fetch: Attempts Live API first, falls back to Local JSON.
    """
    data = None
    
    # 1. Attempt LIVE API CALL
    if source == "api":
        try:
            api_key = os.environ.get('BLUEGAMMA_API_KEY')
            # If no key is found, trigger the fallback immediately
            if not api_key:
                raise ValueError("No API Key found")
                
            url = "https://www.bluegamma.io" # Example endpoint
            response = requests.get(url, headers={"X-API-Key": api_key}, timeout=5)
            response.raise_for_status() # Check for 404/500 errors
            data = response.json()
            source_label = "Live API"
        except Exception as e:
            print(f"API Fetch failed: {e}. Falling back to local seed...")
            source = "local"

    # 2. Fallback to LOCAL SEED (market_data_test.json)
    if source == "local":
        try:
            # Assume file is in project root
            with open('market_data_test.json') as f:
                data = json.load(f)
            source_label = "Local Seed File"
        except FileNotFoundError:
            return "Error: No market data file found for fallback."

    # 3. Process with PANDAS
    if not data:
        return "No data to process."

    df = pd.DataFrame(data['curve'])
    val_date = data['valuation_date']
    index = data['index']

    # 4. Prepare for Database (Bulk Create)
    rates_to_create = []
    for _, row in df.iterrows():
        rates_to_create.append(
            HistoricalRate(
                date=val_date,
                index_name=index,
                tenor=row['tenor'],
                rate=row['rate']
            )
        )
    
    # 5. Bulk Create to prevent duplicates
    HistoricalRate.objects.bulk_create(rates_to_create, ignore_conflicts=True)
    
    return f"Successfully imported {len(rates_to_create)} rates for {index} from {source_label}."

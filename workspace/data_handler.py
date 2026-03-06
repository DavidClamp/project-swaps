import os
import json
import pandas as pd
import requests
from .models import HistoricalRate

def import_bluegamma_data(source="local"):
    """
    Fetches data from local JSON or BlueGamma API and saves to DB.
    """
    if source == "local":
        with open('market_data_test.json') as f:
            data = json.load(f)
    else:
        # LIVE API CALL (Requires BlueGamma API Key)
        api_key = os.environ.get('BLUEGAMMA_API_KEY')
        url = "https://www.bluegamma.io"
        response = requests.get(url, headers={"X-API-Key": api_key})
        data = response.json()

    # Process with PANDAS (The 'Distinction' Step)
    df = pd.DataFrame(data['curve'])
    val_date = data['valuation_date']
    index = data['index']

    # Bulk Create in Django (Avoids individual save() calls)
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
    
    # Update or Create logic to prevent duplicates
    HistoricalRate.objects.bulk_create(rates_to_create, ignore_conflicts=True)
    return f"Successfully imported {len(rates_to_create)} rates for {index}."

import json
import os
import django
from workspace.models import HistoricalRate

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'swapanalyser.settings')
django.setup()


def load_golden_source():
    file_path = 'workspace/fixtures/testing_default.json'
    with open(file_path, 'r') as f:
        raw_data = json.load(f)
    # BlueGamma check: Find the list if it's nested
    if isinstance(raw_data, dict):
        # Common keys are 'results', 'data', or 'rates'
        data = raw_data.get('results') or raw_data.get('data')
        or raw_data.get('rates') or []
    else:
        data = raw_data

    print(f"Starting import of {len(data)} rows...")

    for item in data:
        # Final safety check: skip if item is just a string
        if not isinstance(item, dict):
            continue

        HistoricalRate.objects.update_or_create(
            date=item.get('date'),
            tenor=item.get('tenor'),
            index_name=item.get('index_name', 'SOFR'),
            defaults={'rate': item.get('rate')}
        )

    print(f"SUCCESS: Imported {HistoricalRate.objects.count()} rows!")


if __name__ == "__main__":
    load_golden_source()

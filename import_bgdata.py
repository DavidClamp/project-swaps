import json
import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'swapanalyser.settings')
django.setup()

from workspace.models import HistoricalRate

def load_golden_source():
    file_path = 'workspace/fixtures/testing_default.json'
    
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    print(f"Starting import of {len(data)} rows...")
    
    count = 0
    for item in data:
        # Map your JSON fields to your Django Model fields
        # Adjusted for BlueGamma flat JSON format
        HistoricalRate.objects.update_or_create(
            date=item['date'],
            tenor=item['tenor'],
            index_name=item.get('index_name', 'SOFR'),
            defaults={'rate': item['rate']}
        )
        count += 1
        if count % 500 == 0:
            print(f"Processed {count} rows...")

    print(f"SUCCESS: Imported {count} rows into the database!")

if __name__ == "__main__":
    load_golden_source()

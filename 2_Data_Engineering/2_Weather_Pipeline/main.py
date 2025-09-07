import sys
import csv
import os
from datetime import date, timedelta
from typing import List

from create_tables import create_tables
from weather_utils import fetch_hourly_weather, WeatherAPIError
from hourly_weather import insert_weather_data
from daily_weather import aggregate_daily
from global_weather import aggregate_global

CSV_DEFAULT = "india_cities.csv"
DB_PATH = "data.db"

def load_cities(csv_path: str) -> List[str]:
    cities = []
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        # Expecting a column named "city" (case-insensitive ok)
        first_row = next(reader, None)
        if first_row is None:
            return []
        # Normalize header detection
        headers = [h.lower() for h in reader.fieldnames or []]
        if "city" not in headers:
            raise ValueError("CSV must have a 'city' column")

        # include first row
        if first_row:
            cities.append(first_row[[h for h in reader.fieldnames if h.lower()=="city"][0]].strip())
        for row in reader:
            city = row[[h for h in reader.fieldnames if h.lower()=="city"][0]].strip()
            if city:
                cities.append(city)
    # de-dup & preserve order
    seen = set()
    out = []
    for c in cities:
        if c not in seen:
            seen.add(c)
            out.append(c)
    return out

def main():
    # Usage: python main.py [YYYY-MM-DD] [CSV_PATH] [DB_PATH]
    # If date omitted, default to yesterday (to ensure full-day history is available)
    run_date = None
    if len(sys.argv) >= 2:
        run_date = sys.argv[1]
    else:
        run_date = (date.today() - timedelta(days=1)).strftime("%Y-%m-%d")

    csv_path = sys.argv[2] if len(sys.argv) >= 3 else CSV_DEFAULT
    db_path = sys.argv[3] if len(sys.argv) >= 4 else DB_PATH

    # Create tables
    create_tables(db_path)

    # Load cities
    cities = load_cities(csv_path)

    # Optional cap for testing
    max_cities_env = os.getenv("MAX_CITIES", "").strip()
    if max_cities_env.isdigit():
        cities = cities[:int(max_cities_env)]

    total_inserted = 0
    for city in cities:
        try:
            hourly = fetch_hourly_weather(city, run_date)
            if not hourly:
                print(f"[WARN] No data for {city} on {run_date}")
                continue
            inserted = insert_weather_data(hourly, db_path=db_path)
            total_inserted += inserted
            print(f"[OK] {city}: inserted {inserted} hourly rows")
        except WeatherAPIError as e:
            print(f"[API ERROR] {city}: {e}")
        except Exception as e:
            print(f"[ERROR] {city}: {e}")

    # Transformations
    daily_rows = aggregate_daily(db_path=db_path)
    global_rows = aggregate_global(db_path=db_path)

    print(f"Hourly inserted: {total_inserted}")
    print(f"Daily upserts:  {daily_rows}")
    print(f"Global upserts: {global_rows}")
    print("ETL run complete.")

if __name__ == "__main__":
    main()

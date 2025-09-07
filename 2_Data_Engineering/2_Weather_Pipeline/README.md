# Indian Weather ETL

A modular ETL pipeline that fetches hourly historical weather for Indian cities from WeatherAPI, stores raw data in SQLite, aggregates it to daily insights, then maintains rolling city averages. Includes a Matplotlib notebook for stakeholder-ready visuals.

## Project Structure

```
.
├── main.py               # Orchestrates the ETL process
├── create_tables.py      # Creates all database tables
├── weather_utils.py      # Extracts weather data via WeatherAPI
├── hourly_weather.py     # Saves hourly records into database
├── daily_weather.py      # Aggregates hourly to daily
├── global_weather.py     # Aggregates daily to city-wide averages
├── india_cities.csv      # List of cities to process (expects a 'city' column)
├── requirements.txt
├── .env
├── data.db               # SQLite database (created after first run)
└── visualization.ipynb   # Explore insights & answer stakeholder questions
```

## Quickstart

1. **Install deps** (Python 3.10+ recommended):
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure `.env`**:
   ```bash
   cp .env.example .env
   # paste your WeatherAPI key into WEATHERAPI_KEY
   ```

3. **Run ETL for yesterday** (default):
   ```bash
   python main.py
   ```

   Or for a specific date (must not be future):
   ```bash
   python main.py 2025-09-01
   ```

   Optional:
   ```bash
   # Process only first N cities while testing
   export MAX_CITIES=5
   ```

4. **Open the notebook** `visualization.ipynb` and run the cells to generate visuals from your SQLite DB (`data.db`).

## Notes
- We use `INSERT OR IGNORE` for de-duping hourly data.
- We use `UPSERT (ON CONFLICT)` to refresh aggregates in `daily_weather` and `global_weather`.
- If you change DB filename, pass it as the 3rd CLI argument in `main.py` or adjust scripts accordingly.

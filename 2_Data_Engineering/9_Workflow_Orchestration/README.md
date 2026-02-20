# 🌤️ Weather Data Pipeline — Dagster

A **production-quality ETL pipeline** built with [Dagster](https://dagster.io/) that:
- **Fetches** 24-hour historical weather data from [Open-Meteo](https://open-meteo.com/) (free, no API key required)
- **Stores** it in a local SQLite database (`data.db`)
- **Aggregates** hourly → daily → global weather summaries
- **Visualises** the full data lineage in Dagster's asset graph UI

---

## Architecture

```
setup_database → fetch_weather → fetch_daily_weather → global_weather
     ↓                ↓                  ↓                    ↓
  SQLite tables   weather table     daily_weather        global_weather
  (3 tables)      (24 hourly rows)  (daily averages)     (cross-city)
```

## Project Structure

```
weather_project/
├── .env                     ← Configure CITY, TARGET_DATE, DB_PATH
├── data.db                  ← SQLite database (auto-created)
├── pyproject.toml           ← Package & dependency config
├── src/
│   └── dagster_quickstart/
│       ├── assets.py        ← 4 Dagster @asset functions (THE CORE)
│       ├── definitions.py   ← Dagster Definitions entry point
│       ├── defs/
│       └── utils/
│           ├── tables.py         ← DB schema creation
│           ├── weather_utils.py  ← Open-Meteo API fetcher
│           ├── hourly_weather.py ← Hourly data → SQLite inserts
│           ├── daily_weather.py  ← Hourly → daily aggregation
│           └── global_weather.py ← Daily → global aggregation
└── tests/
```

## Quick Start

### 1. Install dependencies

```bash
# Using pip (recommended for first run)
pip install -e ".[dev]"

# OR using uv
uv sync
```

### 2. Configure your pipeline

Edit `.env`:
```dotenv
CITY=Mumbai
TARGET_DATE=2025-01-15
DB_PATH=data.db
```

### 3. Launch Dagster UI

```bash
# From the weather_project directory
dagster dev
```

Then open **http://localhost:3000** in your browser.

### 4. Materialise assets

In the Dagster UI:
1. Go to the **Assets** tab
2. Click **Materialize All**
3. Watch all 4 assets go green ✅

---

## Assets

| Asset | Depends On | What It Does |
|---|---|---|
| `setup_database` | — | Creates 3 SQLite tables |
| `fetch_weather` | `setup_database` | Fetches 24h of hourly data from Open-Meteo |
| `fetch_daily_weather` | `fetch_weather` | Aggregates hourly → daily averages |
| `global_weather` | `fetch_daily_weather` | Aggregates daily → global summary |

---

## Data API

Uses **Open-Meteo Archive API** — completely free, no API key needed:
- Endpoint: `https://archive-api.open-meteo.com/v1/archive`
- Variables: `temperature_2m`, `relative_humidity_2m`, `wind_speed_10m`, `precipitation`

---

*DataMonk Internship — Data Engineering Track | Project 9: Workflow Orchestration*

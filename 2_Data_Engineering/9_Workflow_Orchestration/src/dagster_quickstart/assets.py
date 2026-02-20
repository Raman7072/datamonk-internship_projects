"""
assets.py — Dagster Software-Defined Assets for the Weather Data Pipeline.

Asset execution order (enforced via `deps`):
    setup_database → fetch_weather → fetch_daily_weather → global_weather

Each asset returns a MaterializeResult with metadata visible in the Dagster UI.
"""

import os

from dotenv import load_dotenv

from dagster import asset, MaterializeResult, MetadataValue

from .utils.tables import create_table
from .utils.weather_utils import fetch_hourly_weather
from .utils.hourly_weather import insert_hourly_rows
from .utils.daily_weather import fetch_day_average
from .utils.global_weather import fetch_global_average

# ── Load .env configuration ───────────────────────────────────────────────────
load_dotenv()

CITY: str = os.getenv("CITY", "Mumbai")
TARGET_DATE: str = os.getenv("TARGET_DATE", "2025-01-15")


# ─────────────────────────────────────────────────────────────────────────────
# Asset 1 — setup_database
# ─────────────────────────────────────────────────────────────────────────────
@asset(
    name="setup_database",
    group_name="weather_pipeline",
    description=(
        "Initialises the SQLite database with three tables: "
        "`weather` (hourly), `daily_weather`, and `global_weather`. "
        "Safe to re-run — uses CREATE TABLE IF NOT EXISTS."
    ),
)
def setup_database() -> MaterializeResult:
    """Create all required SQLite tables."""
    create_table()
    return MaterializeResult(
        metadata={
            "tables_created": MetadataValue.text(
                "weather | daily_weather | global_weather"
            ),
            "db_path": MetadataValue.text(os.getenv("DB_PATH", "data.db")),
            "status": MetadataValue.text("✅ Schema initialised successfully"),
        }
    )


# ─────────────────────────────────────────────────────────────────────────────
# Asset 2 — fetch_weather
# ─────────────────────────────────────────────────────────────────────────────
@asset(
    name="fetch_weather",
    deps=[setup_database],
    group_name="weather_pipeline",
    description=(
        f"Fetches 24-hour historical weather for {CITY} on {TARGET_DATE} "
        "from Open-Meteo Archive API (no API key required) and stores "
        "records into the `weather` table."
    ),
)
def fetch_weather() -> MaterializeResult:
    """Fetch hourly weather from Open-Meteo and persist to SQLite."""
    hourly_rows = fetch_hourly_weather(CITY, TARGET_DATE)
    inserted = insert_hourly_rows(CITY, TARGET_DATE, hourly_rows)

    # Build a quick preview of the first few rows
    preview_lines = ["| hour  | temp_c | humidity% | wind_kmh | precip_mm |", "|-------|--------|-----------|----------|-----------|"]
    for row in hourly_rows[:6]:
        preview_lines.append(
            f"| {row['hour']} | {row['temp_c']} | {row['humidity_pct']} | {row['wind_kmh']} | {row['precip_mm']} |"
        )
    preview_lines.append(f"| … ({len(hourly_rows)} rows total) | | | | |")

    return MaterializeResult(
        metadata={
            "city": MetadataValue.text(CITY),
            "date": MetadataValue.text(TARGET_DATE),
            "total_hours_fetched": MetadataValue.int(len(hourly_rows)),
            "rows_inserted": MetadataValue.int(inserted),
            "preview": MetadataValue.md("\n".join(preview_lines)),
            "source": MetadataValue.url(
                "https://archive-api.open-meteo.com/v1/archive"
            ),
        }
    )


# ─────────────────────────────────────────────────────────────────────────────
# Asset 3 — fetch_daily_weather
# ─────────────────────────────────────────────────────────────────────────────
@asset(
    name="fetch_daily_weather",
    deps=[fetch_weather],
    group_name="weather_pipeline",
    description=(
        "Aggregates hourly records in `weather` into per-day averages "
        "and upserts them into `daily_weather`."
    ),
)
def fetch_daily_weather() -> MaterializeResult:
    """Compute daily averages and store them in daily_weather."""
    df = fetch_day_average(CITY)

    if df.empty:
        return MaterializeResult(
            metadata={
                "warning": MetadataValue.text(
                    f"No hourly data found for {CITY}. Run fetch_weather first."
                )
            }
        )

    return MaterializeResult(
        metadata={
            "city": MetadataValue.text(CITY),
            "dates_processed": MetadataValue.int(len(df)),
            "preview": MetadataValue.md(df.to_markdown(index=False)),
        }
    )


# ─────────────────────────────────────────────────────────────────────────────
# Asset 4 — global_weather
# ─────────────────────────────────────────────────────────────────────────────
@asset(
    name="global_weather",
    deps=[fetch_daily_weather],
    group_name="weather_pipeline",
    description=(
        "Computes a cross-date global weather summary for the city from "
        "`daily_weather` and appends it to `global_weather`. Each pipeline "
        "run adds a timestamped snapshot to track evolution over time."
    ),
)
def global_weather() -> MaterializeResult:
    """Aggregate daily data into a global summary and persist it."""
    df = fetch_global_average(CITY.title())

    if df.empty:
        return MaterializeResult(
            metadata={
                "warning": MetadataValue.text(
                    f"No daily data found for {CITY}. Run fetch_daily_weather first."
                )
            }
        )

    return MaterializeResult(
        metadata={
            "city": MetadataValue.text(CITY),
            "global_summary": MetadataValue.md(df.to_markdown(index=False)),
            "status": MetadataValue.text("✅ Global summary appended to global_weather"),
        }
    )

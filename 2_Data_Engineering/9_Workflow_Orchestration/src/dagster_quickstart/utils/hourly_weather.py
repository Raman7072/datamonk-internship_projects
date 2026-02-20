"""
hourly_weather.py — Insert hourly weather rows into the `weather` SQLite table.
"""

from datetime import datetime, timezone
from typing import Any

from .tables import get_connection


def insert_hourly_rows(city: str, date: str, rows: list[dict[str, Any]]) -> int:
    """
    Bulk-insert hourly weather records into the `weather` table.

    Uses INSERT OR IGNORE so re-running the pipeline on the same city+date is safe.

    Args:
        city : City name, e.g. "Mumbai"
        date : ISO date string, e.g. "2025-01-15"
        rows : List of dicts from weather_utils.fetch_hourly_weather()

    Returns:
        Number of rows actually inserted (ignores duplicates).
    """
    conn = get_connection()
    cursor = conn.cursor()
    fetched_at = datetime.now(timezone.utc).isoformat()
    inserted = 0

    for row in rows:
        result = cursor.execute(
            """
            INSERT OR IGNORE INTO weather
                (city, date, hour, temp_c, humidity_pct, wind_kmh, precip_mm, fetched_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                city,
                date,
                row["hour"],
                row.get("temp_c"),
                row.get("humidity_pct"),
                row.get("wind_kmh"),
                row.get("precip_mm"),
                fetched_at,
            ),
        )
        inserted += result.rowcount  # 1 if inserted, 0 if ignored

    conn.commit()
    conn.close()
    print(f"[hourly_weather] ✅ Inserted {inserted}/{len(rows)} rows for {city} on {date}.")
    return inserted

"""
global_weather.py — Aggregate daily city averages into a global weather summary.

Reads from `daily_weather`, groups across all cities, and inserts a
per-city global summary row into the `global_weather` table.
"""

from datetime import datetime, timezone

import pandas as pd

from .tables import get_connection


def fetch_global_average(city: str) -> pd.DataFrame:
    """
    Compute a global weather summary for the specified city from the
    `daily_weather` table and write it to `global_weather`.

    This models a real-world scenario where each pipeline run contributes
    one city's averaged metrics to a growing cross-city summary.

    Args:
        city : City name used to filter the daily_weather table.

    Returns:
        pandas DataFrame of the rows inserted into global_weather.
    """
    conn = get_connection()
    computed_at = datetime.now(timezone.utc).isoformat()

    # ── Aggregate daily → global (city-level summary) ────────────────────────
    query = """
        SELECT
            city,
            AVG(avg_temp_c)      AS avg_temp_c,
            AVG(avg_humidity)    AS avg_humidity,
            AVG(avg_wind_kmh)    AS avg_wind_kmh,
            SUM(total_precip_mm) AS total_precip_mm
        FROM daily_weather
        WHERE city = ?
        GROUP BY city
    """
    df = pd.read_sql_query(query, conn, params=(city,))

    if df.empty:
        print(f"[global_weather] ⚠️  No daily records found for '{city}' to globalise.")
        conn.close()
        return df

    # ── Insert into global_weather (append — tracks history over runs) ───────
    cursor = conn.cursor()
    for _, row in df.iterrows():
        cursor.execute(
            """
            INSERT INTO global_weather
                (computed_at, city, avg_temp_c, avg_humidity, avg_wind_kmh, total_precip_mm)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                computed_at,
                row["city"],
                round(row["avg_temp_c"], 2) if row["avg_temp_c"] is not None else None,
                round(row["avg_humidity"], 2) if row["avg_humidity"] is not None else None,
                round(row["avg_wind_kmh"], 2) if row["avg_wind_kmh"] is not None else None,
                round(row["total_precip_mm"], 3) if row["total_precip_mm"] is not None else None,
            ),
        )
    conn.commit()
    conn.close()

    df["computed_at"] = computed_at
    df = df.round({"avg_temp_c": 2, "avg_humidity": 2, "avg_wind_kmh": 2, "total_precip_mm": 3})

    print(f"[global_weather] ✅ Global summary inserted for {city}.")
    return df

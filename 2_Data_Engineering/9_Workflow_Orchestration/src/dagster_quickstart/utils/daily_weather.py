"""
daily_weather.py — Aggregate hourly weather records into daily averages.

Reads from the `weather` table, computes per-city-per-date averages,
and upserts the results into `daily_weather`.

Returns a pandas DataFrame of processed rows for Dagster metadata previews.
"""

from datetime import datetime, timezone

import pandas as pd

from .tables import get_connection


def fetch_day_average(city: str) -> pd.DataFrame:
    """
    Compute daily averages for the given city from hourly records
    and upsert into the `daily_weather` table.

    Args:
        city : City name (exact match used for SQL WHERE clause).

    Returns:
        pandas DataFrame of the rows that were computed, with columns:
        [city, date, avg_temp_c, avg_humidity, avg_wind_kmh, total_precip_mm, computed_at]
    """
    conn = get_connection()
    computed_at = datetime.now(timezone.utc).isoformat()

    # ── Aggregate hourly → daily ─────────────────────────────────────────────
    query = """
        SELECT
            city,
            date,
            AVG(temp_c)       AS avg_temp_c,
            AVG(humidity_pct) AS avg_humidity,
            AVG(wind_kmh)     AS avg_wind_kmh,
            SUM(precip_mm)    AS total_precip_mm
        FROM weather
        WHERE city = ?
        GROUP BY city, date
        ORDER BY date
    """
    df = pd.read_sql_query(query, conn, params=(city,))

    if df.empty:
        print(f"[daily_weather] ⚠️  No hourly records found for city '{city}'.")
        conn.close()
        return df

    # ── Upsert into daily_weather ────────────────────────────────────────────
    cursor = conn.cursor()
    for _, row in df.iterrows():
        cursor.execute(
            """
            INSERT INTO daily_weather
                (city, date, avg_temp_c, avg_humidity, avg_wind_kmh, total_precip_mm, computed_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(city, date) DO UPDATE SET
                avg_temp_c      = excluded.avg_temp_c,
                avg_humidity    = excluded.avg_humidity,
                avg_wind_kmh    = excluded.avg_wind_kmh,
                total_precip_mm = excluded.total_precip_mm,
                computed_at     = excluded.computed_at
            """,
            (
                row["city"],
                row["date"],
                round(row["avg_temp_c"], 2) if row["avg_temp_c"] is not None else None,
                round(row["avg_humidity"], 2) if row["avg_humidity"] is not None else None,
                round(row["avg_wind_kmh"], 2) if row["avg_wind_kmh"] is not None else None,
                round(row["total_precip_mm"], 3) if row["total_precip_mm"] is not None else None,
                computed_at,
            ),
        )
    conn.commit()
    conn.close()

    # Add computed_at column to the returned DataFrame for display
    df["computed_at"] = computed_at
    df = df.round({"avg_temp_c": 2, "avg_humidity": 2, "avg_wind_kmh": 2, "total_precip_mm": 3})

    print(f"[daily_weather] ✅ Computed daily averages for {city}: {len(df)} date(s).")
    return df

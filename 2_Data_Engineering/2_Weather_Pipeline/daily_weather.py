import sqlite3

def aggregate_daily(db_path: str = "data.db") -> int:
    """Aggregate hourly records into daily_weather. Returns rows upserted."""
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # Compute per-day aggregates from raw "weather"
    # Use a subquery to calculate aggregates, then UPSERT into daily_weather
    cur.execute("""
        INSERT INTO daily_weather (date, location_name, max_temp, min_temp, avg_humidity)
        SELECT
            date,
            location_name,
            MAX(temperature) AS max_temp,
            MIN(temperature) AS min_temp,
            AVG(humidity)    AS avg_humidity
        FROM weather
        GROUP BY location_name, date
        ON CONFLICT(location_name, date) DO UPDATE SET
            max_temp=excluded.max_temp,
            min_temp=excluded.min_temp,
            avg_humidity=excluded.avg_humidity;
    """)

    rows = cur.rowcount if cur.rowcount is not None else 0
    conn.commit()
    conn.close()
    return rows

import sqlite3
from datetime import datetime

def aggregate_global(db_path: str = "data.db") -> int:
    """Aggregate daily_weather into global_weather rolling averages. Returns rows upserted."""
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # Compute city-level averages across all available days
    cur.execute("""
        INSERT INTO global_weather (location_name, avg_max_temp, avg_min_temp, avg_humidity, updated_at)
        SELECT
            location_name,
            AVG(max_temp) AS avg_max_temp,
            AVG(min_temp) AS avg_min_temp,
            AVG(avg_humidity) AS avg_humidity,
            ? as updated_at
        FROM daily_weather
        GROUP BY location_name
        ON CONFLICT(location_name) DO UPDATE SET
            avg_max_temp=excluded.avg_max_temp,
            avg_min_temp=excluded.avg_min_temp,
            avg_humidity=excluded.avg_humidity,
            updated_at=excluded.updated_at;
    """, (datetime.utcnow().isoformat(timespec="seconds")+"Z",))

    rows = cur.rowcount if cur.rowcount is not None else 0
    conn.commit()
    conn.close()
    return rows

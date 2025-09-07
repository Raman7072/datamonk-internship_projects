import sqlite3

def create_tables(db_path: str = "data.db") -> None:
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # Raw hourly weather data
    cur.execute("""
    CREATE TABLE IF NOT EXISTS weather (
        date TEXT NOT NULL,                 -- YYYY-MM-DD (local date of the record)
        time TEXT NOT NULL,                 -- local hour timestamp (e.g., 2025-09-01 13:00)
        temperature REAL,
        condition TEXT,
        humidity REAL,
        location_name TEXT NOT NULL,
        region TEXT,
        country TEXT,
        latitude REAL,
        longitude REAL,
        local_time TEXT,                    -- provider's reported local time string
        PRIMARY KEY (location_name, time)   -- de-duplicate on city+hour
    );
    """)

    # Aggregated daily weather by city & date
    cur.execute("""
    CREATE TABLE IF NOT EXISTS daily_weather (
        date TEXT NOT NULL,
        location_name TEXT NOT NULL,
        max_temp REAL,
        min_temp REAL,
        avg_humidity REAL,
        PRIMARY KEY (location_name, date)
    );
    """)

    # Long-term rolling averages by city
    cur.execute("""
    CREATE TABLE IF NOT EXISTS global_weather (
        location_name TEXT PRIMARY KEY,
        avg_max_temp REAL,
        avg_min_temp REAL,
        avg_humidity REAL,
        updated_at TEXT
    );
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
    print("Tables created (or already exist).")

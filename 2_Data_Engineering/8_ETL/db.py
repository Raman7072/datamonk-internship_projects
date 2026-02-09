import sqlite3
import logging

logger = logging.getLogger(__name__)

DB_PATH = "weather.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather (
            city TEXT,
            date TEXT,
            hour INTEGER,
            temperature REAL,
            humidity INTEGER,
            PRIMARY KEY (city, date, hour)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS daily_weather (
            city TEXT,
            date TEXT,
            avg_temp REAL,
            avg_humidity REAL,
            PRIMARY KEY (city, date)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS global_weather (
            date TEXT PRIMARY KEY,
            global_avg_temp REAL,
            global_avg_humidity REAL
        )
    """)

    conn.commit()
    conn.close()

    logger.info("All tables created successfully")

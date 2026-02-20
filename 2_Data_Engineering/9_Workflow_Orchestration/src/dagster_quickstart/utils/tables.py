"""
tables.py — SQLite schema initialization for the Weather Pipeline.

Creates three tables if they don't already exist:
  - weather        : raw hourly observations per city/date
  - daily_weather  : daily averages aggregated from hourly data
  - global_weather : global summary across all cities
"""

import sqlite3
import os


def get_db_path() -> str:
    """Resolve the SQLite DB path from env or default."""
    db_path = os.getenv("DB_PATH", "data.db")
    # If it's a relative path, resolve from the weather_project root
    # (the cwd when dagster dev is invoked)
    return db_path


def get_connection() -> sqlite3.Connection:
    """Return a connection to the SQLite database."""
    conn = sqlite3.connect(get_db_path())
    conn.row_factory = sqlite3.Row
    return conn


def create_table() -> None:
    """
    Initialize all three pipeline tables. Safe to call multiple times
    (uses CREATE TABLE IF NOT EXISTS).
    """
    conn = get_connection()
    cursor = conn.cursor()

    # ── 1. Hourly weather observations ──────────────────────────────────────
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS weather (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            city        TEXT    NOT NULL,
            date        TEXT    NOT NULL,   -- YYYY-MM-DD
            hour        TEXT    NOT NULL,   -- HH:MM
            temp_c      REAL,
            humidity_pct REAL,
            wind_kmh    REAL,
            precip_mm   REAL,
            fetched_at  TEXT    NOT NULL,
            UNIQUE(city, date, hour)        -- prevent duplicate rows
        )
        """
    )

    # ── 2. Daily aggregated weather ──────────────────────────────────────────
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS daily_weather (
            id            INTEGER PRIMARY KEY AUTOINCREMENT,
            city          TEXT NOT NULL,
            date          TEXT NOT NULL,    -- YYYY-MM-DD
            avg_temp_c    REAL,
            avg_humidity  REAL,
            avg_wind_kmh  REAL,
            total_precip_mm REAL,
            computed_at   TEXT NOT NULL,
            UNIQUE(city, date)
        )
        """
    )

    # ── 3. Global weather summary ────────────────────────────────────────────
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS global_weather (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            computed_at     TEXT NOT NULL,
            city            TEXT NOT NULL,
            avg_temp_c      REAL,
            avg_humidity    REAL,
            avg_wind_kmh    REAL,
            total_precip_mm REAL
        )
        """
    )

    conn.commit()
    conn.close()
    print("[tables] ✅ All tables created / verified.")

import logging
from db import get_connection

logger = logging.getLogger(__name__)


def fetch_day_average():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR REPLACE INTO daily_weather
        SELECT
            city,
            date,
            AVG(temperature),
            AVG(humidity)
        FROM weather
        GROUP BY city, date
    """)

    conn.commit()
    conn.close()

    logger.info("Daily weather aggregation completed")


def fetch_global_average():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR REPLACE INTO global_weather
        SELECT
            date,
            AVG(avg_temp),
            AVG(avg_humidity)
        FROM daily_weather
        GROUP BY date
    """)

    conn.commit()
    conn.close()

    logger.info("Global weather aggregation completed")

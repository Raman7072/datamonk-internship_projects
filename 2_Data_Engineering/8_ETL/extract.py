import requests
import logging
from db import get_connection
import os
from dotenv import load_dotenv
load_dotenv()

logger = logging.getLogger(__name__)

API_KEY = os.getenv("WEATHERAPI_KEY", "").strip()
BASE_URL = "https://api.weatherapi.com/v1/history.json"


def fetch_and_store_weather(city: str, date: str):
    params = {
        "key": API_KEY,
        "q": city,
        "dt": date
    }

    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()

    data = response.json()
    hours = data["forecast"]["forecastday"][0]["hour"]

    conn = get_connection()
    cursor = conn.cursor()

    for h in hours:
        cursor.execute("""
            INSERT OR IGNORE INTO weather
            (city, date, hour, temperature, humidity)
            VALUES (?, ?, ?, ?, ?)
        """, (
            city,
            date,
            int(h["time"].split(" ")[1].split(":")[0]),
            h["temp_c"],
            h["humidity"]
        ))

    conn.commit()
    conn.close()

    logger.info("Weather data fetched for %s on %s", city, date)

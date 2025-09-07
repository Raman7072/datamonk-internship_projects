import os
import time
from datetime import datetime, date
from typing import Dict, Any, List

import requests
from dotenv import load_dotenv

# WeatherAPI docs: https://www.weatherapi.com/docs/
# We'll use the "History" endpoint to get hourly data for a specific past date.
# Endpoint: http://api.weatherapi.com/v1/history.json?key=KEY&q=CITY&dt=YYYY-MM-DD

load_dotenv()

API_KEY = os.getenv("WEATHERAPI_KEY", "").strip()
BASE_URL = "http://api.weatherapi.com/v1/history.json"

class WeatherAPIError(Exception):
    pass

def _validate_date_str(date_str: str) -> str:
    try:
        d = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError as e:
        raise ValueError("date must be in YYYY-MM-DD format") from e

    if d > date.today():
        raise ValueError("Date cannot be in the future.")
    return date_str

def fetch_hourly_weather(city: str, date_str: str) -> List[Dict[str, Any]]:
    if not API_KEY:
        raise WeatherAPIError("Missing WEATHERAPI_KEY in environment or .env file.")

    date_str = _validate_date_str(date_str)

    params = {
        "key": API_KEY,
        "q": city,
        "dt": date_str,
        "aqi": "no",
        "alerts": "no",
    }

    resp = requests.get(BASE_URL, params=params, timeout=30)
    if resp.status_code != 200:
        raise WeatherAPIError(f"API request failed ({resp.status_code}): {resp.text}")

    payload = resp.json()

    # Defensive checks on payload structure
    location = payload.get("location", {}) or {}
    forecast = payload.get("forecast", {}) or {}
    forecastday = (forecast.get("forecastday") or [])
    if not forecastday:
        return []

    hours = forecastday[0].get("hour") or []
    results = []
    for h in hours:
        # Only keep the specified fields
        results.append({
            "date": date_str,
            "time": h.get("time"),  # e.g. "2025-09-01 13:00"
            "temperature": h.get("temp_c"),
            "condition": (h.get("condition") or {}).get("text"),
            "humidity": h.get("humidity"),
            "location_name": location.get("name"),
            "region": location.get("region"),
            "country": location.get("country"),
            "latitude": location.get("lat"),
            "longitude": location.get("lon"),
            "local_time": location.get("localtime"),
        })
    return results

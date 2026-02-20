"""
weather_utils.py — Fetch raw hourly weather data using WeatherAPI.com.

Free plan: supports current.json and forecast.json (today + up to 3 days ahead).
Paid plan: supports history.json (past dates).

WEATHERAPI_KEY must be set in .env.
API docs: https://www.weatherapi.com/docs/
"""

import os
from datetime import date
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()

FORECAST_URL = "http://api.weatherapi.com/v1/forecast.json"
HISTORY_URL  = "http://api.weatherapi.com/v1/history.json"


def fetch_hourly_weather(city: str, target_date: str) -> list[dict[str, Any]]:
    """
    Fetch 24-hour weather data for a city on a given date using WeatherAPI.com.

    - For today or future dates (within 3 days): uses the free forecast endpoint.
    - For past dates                            : uses the history endpoint (paid plan).

    Args:
        city        : City name, e.g. "Mumbai"
        target_date : ISO date string "YYYY-MM-DD"

    Returns:
        List of up to 24 dicts, one per hour:
        {
            "hour"        : "HH:MM",
            "temp_c"      : float,
            "humidity_pct": float,
            "wind_kmh"    : float,
            "precip_mm"   : float,
        }
    """
    api_key = os.getenv("WEATHERAPI_KEY", "").strip()
    if not api_key:
        raise ValueError(
            "[weather_utils] WEATHERAPI_KEY is not set. "
            "Add it to your .env file: WEATHERAPI_KEY=your_key_here"
        )

    today = date.today().isoformat()
    use_forecast = target_date >= today   # free tier works for today / future

    url    = FORECAST_URL if use_forecast else HISTORY_URL
    params = {"key": api_key, "q": city, "dt": target_date}
    if use_forecast:
        params["days"] = 1          # only need today's 24 hours

    print(f"[weather_utils] 🌐 Fetching {'forecast' if use_forecast else 'history'} "
          f"for {city} on {target_date} ...")

    resp = requests.get(url, params=params, timeout=30)

    if resp.status_code != 200:
        try:
            err_msg = resp.json().get("error", {}).get("message", resp.text)
        except Exception:
            err_msg = resp.text
        raise ValueError(
            f"[weather_utils] WeatherAPI error {resp.status_code}: {err_msg}\n"
            f"Note: Historical data requires a paid WeatherAPI plan. "
            f"Set TARGET_DATE to today or a future date to use the free forecast endpoint."
        )

    data = resp.json()

    try:
        hourly_list = data["forecast"]["forecastday"][0]["hour"]
    except (KeyError, IndexError) as exc:
        raise ValueError(
            f"[weather_utils] Unexpected API response structure: {exc}"
        ) from exc

    rows: list[dict[str, Any]] = []
    for h in hourly_list:
        time_str = h.get("time", "")
        hour = time_str.split(" ")[1] if " " in time_str else "00:00"
        rows.append(
            {
                "hour"        : hour,
                "temp_c"      : h.get("temp_c"),
                "humidity_pct": float(h.get("humidity", 0)),
                "wind_kmh"    : h.get("wind_kph"),
                "precip_mm"   : h.get("precip_mm"),
            }
        )

    print(f"[weather_utils] ✅ Fetched {len(rows)} hourly records for {city} on {target_date}.")
    return rows

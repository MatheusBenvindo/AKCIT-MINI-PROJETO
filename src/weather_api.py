"""
SkyMetrics - Weather API Interaction
"""
import os
import requests
from typing import Dict, Any

class WeatherAPIError(Exception):
    """Custom exception for API errors."""
    pass

def get_weather_data(city_name: str) -> Dict[str, Any]:
    """
    Fetches weather data for a given city from OpenWeatherMap.
    Requires OPENWEATHER_API_KEY environment variable.
    """
    api_key = os.environ.get("OPENWEATHER_API_KEY")
    if not api_key:
        raise WeatherAPIError("OPENWEATHER_API_KEY environment variable is not set.")

    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key
    }

    try:
        response = requests.get(base_url, params=params, timeout=10)
        
        # Handle specific HTTP errors
        if response.status_code == 404:
            raise WeatherAPIError(f"City '{city_name}' not found.")
        elif response.status_code == 401:
            raise WeatherAPIError("Invalid API key.")
        
        response.raise_for_status() # Raise for other 4xx/5xx errors
        
        data = response.json()
        return data

    except requests.exceptions.RequestException as e:
        raise WeatherAPIError(f"Network error occurred while fetching data: {e}")
    except ValueError:
        raise WeatherAPIError("Invalid JSON response from the API.")

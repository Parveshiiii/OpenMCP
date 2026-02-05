import requests
import asyncio

def _fetch_forecast_sync(city_name):
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&language=en&format=json"
    
    try:
        geo_data = requests.get(geo_url).json()
        
        if 'results' not in geo_data:
            return f"Could not find coordinates for: {city_name}"
            
        # Extract Lat/Long and Timezone from the first result
        location = geo_data['results'][0]
        lat = location['latitude']
        lon = location['longitude']
        tz = location.get('timezone', 'auto')

        weather_url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": lat,
            "longitude": lon,
            "current_weather": "true",
            "daily": "temperature_2m_max,temperature_2m_min",
            "timezone": tz
        }
        
        weather_response = requests.get(weather_url, params=params).json()
        return weather_response

    except Exception as e:
        return {"error": str(e)}

async def get_forecast(city_name: str) -> dict:
    """
    Get the current weather forecast for a given city name.
    
    Args:
        city_name (str): The name of the city (e.g., "Paris", "New York").
    """
    return await asyncio.to_thread(_fetch_forecast_sync, city_name)


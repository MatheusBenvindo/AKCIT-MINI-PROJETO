import argparse
import sys
from src.weather_api import get_weather_data, WeatherAPIError
from src.conversions import kelvin_to_celsius, kelvin_to_fahrenheit

def main():
    parser = argparse.ArgumentParser(description="SkyMetrics - CLI Weather App")
    parser.add_argument("city", type=str, help="Name of the city to query")
    
    args = parser.parse_args()
    
    print(f"Fetching weather data for {args.city}...")
    
    try:
        data = get_weather_data(args.city)
        
        # Extract data
        weather_desc = data["weather"][0]["description"].capitalize()
        temp_k = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        city_name = data["name"]
        country = data["sys"]["country"]
        
        # Convert temperatures
        temp_c = kelvin_to_celsius(temp_k)
        temp_f = kelvin_to_fahrenheit(temp_k)
        
        print("\n" + "="*30)
        print(f" Weather in {city_name}, {country}")
        print("="*30)
        print(f" Condition:   {weather_desc}")
        print(f" Temperature: {temp_c} °C / {temp_f} °F")
        print(f" Humidity:    {humidity}%")
        print("="*30 + "\n")
        
    except WeatherAPIError as e:
        print(f"\nError: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()

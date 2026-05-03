import argparse
import sys
from src.weather_api import get_weather_data, WeatherAPIError
from src.conversions import kelvin_to_celsius, kelvin_to_fahrenheit

# Rich visual libraries
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich import box

console = Console()

def get_weather_emoji(description: str) -> str:
    """Returns a related emoji based on the weather description."""
    desc = description.lower()
    if "clear" in desc:
        return "☀️"
    elif "cloud" in desc:
        return "☁️"
    elif "rain" in desc:
        return "🌧️"
    elif "snow" in desc:
        return "❄️"
    elif "thunderstorm" in desc:
        return "⛈️"
    elif "drizzle" in desc:
        return "🌦️"
    else:
        return "🌡️"

def main():
    parser = argparse.ArgumentParser(description="SkyMetrics - CLI Weather App")
    parser.add_argument("city", type=str, help="Name of the city to query")
    
    args = parser.parse_args()
    
    with console.status(f"[bold cyan]Fetching weather data for {args.city}...", spinner="dots"):
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
            
            # Formatting visually with Rich
            emoji = get_weather_emoji(weather_desc)
            
            # Create a table for the metrics
            table = Table(show_header=False, box=box.SIMPLE)
            table.add_column("Metric", style="bold cyan")
            table.add_column("Value", style="bold white")
            
            table.add_row("Condition", f"{emoji} {weather_desc}")
            table.add_row("Temperature", f"[bold yellow]{temp_c} °C[/bold yellow] / [bold green]{temp_f} °F[/bold green]")
            table.add_row("Humidity", f"{humidity}%")
            
            # Wrap everything in a nice panel
            panel = Panel.fit(
                table,
                title=f"[bold blue]SkyMetrics: {city_name}, {country}[/bold blue]",
                border_style="cyan",
                padding=(1, 2)
            )
            
            console.print()
            console.print(panel)
            console.print()
            
        except WeatherAPIError as e:
            console.print(f"\n[bold red]Error:[/bold red] {e}")
            sys.exit(1)
        except Exception as e:
            console.print(f"\n[bold red]An unexpected error occurred:[/bold red] {e}")
            sys.exit(1)

if __name__ == "__main__":
    main()

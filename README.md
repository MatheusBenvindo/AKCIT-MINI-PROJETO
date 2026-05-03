# SkyMetrics

SkyMetrics is a simple, professional command-line interface (CLI) tool to query the current weather of a city using the OpenWeatherMap API. It automatically fetches the temperature, converts it from Kelvin to Celsius and Fahrenheit, and displays the humidity and weather condition.

## Features
- Fast command-line weather queries.
- Automatic conversion from Kelvin to Celsius and Fahrenheit.
- Error handling for missing cities, network issues, and invalid API keys.
- Fully unit-tested conversion logic.

## Project Structure
```
skymetrics/
├── docs/             # Documentation and backlog
├── src/              # Core source code
├── tests/            # Unit tests using pytest
├── main.py           # CLI entry point
└── requirements.txt  # Project dependencies
```

## Prerequisites
- Python 3.8+
- An API key from [OpenWeatherMap](https://openweathermap.org/)

## Installation

1. Clone this repository (or copy the files).
2. Navigate to the project directory:
   ```bash
   cd skymetrics
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Setup

Set up your OpenWeatherMap API key as an environment variable:

**Windows (PowerShell):**
```powershell
$env:OPENWEATHER_API_KEY="your_api_key_here"
```

**Linux/macOS:**
```bash
export OPENWEATHER_API_KEY="your_api_key_here"
```

## Usage

Run the `main.py` script and pass the city name as an argument. Use quotes if the city name has spaces.

```bash
python main.py "São Paulo"
```

**Example Output:**
```
Fetching weather data for São Paulo...

==============================
 Weather in São Paulo, BR
==============================
 Condition:   Clear sky
 Temperature: 28.5 °C / 83.3 °F
 Humidity:    45%
==============================
```

## Testing

To run the unit tests, simply execute `pytest`:

```bash
pytest
```

## Backlog

See `docs/backlog.md` for future improvement ideas.

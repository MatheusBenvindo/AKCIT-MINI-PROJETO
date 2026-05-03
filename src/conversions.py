"""
SkyMetrics - Conversions module
"""

def kelvin_to_celsius(kelvin: float) -> float:
    """Converts Kelvin to Celsius."""
    if kelvin < 0:
        raise ValueError("Temperature in Kelvin cannot be negative.")
    return round(kelvin - 273.15, 2)

def kelvin_to_fahrenheit(kelvin: float) -> float:
    """Converts Kelvin to Fahrenheit."""
    if kelvin < 0:
        raise ValueError("Temperature in Kelvin cannot be negative.")
    celsius = kelvin_to_celsius(kelvin)
    return round((celsius * 9/5) + 32, 2)

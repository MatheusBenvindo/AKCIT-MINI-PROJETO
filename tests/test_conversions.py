import pytest
from src.conversions import kelvin_to_celsius, kelvin_to_fahrenheit

def test_kelvin_to_celsius():
    assert kelvin_to_celsius(273.15) == 0.0
    assert kelvin_to_celsius(300.0) == 26.85
    assert kelvin_to_celsius(0.0) == -273.15

def test_kelvin_to_fahrenheit():
    assert kelvin_to_fahrenheit(273.15) == 32.0
    assert kelvin_to_fahrenheit(300.0) == 80.33
    assert kelvin_to_fahrenheit(0.0) == -459.67

def test_negative_kelvin_celsius():
    with pytest.raises(ValueError):
        kelvin_to_celsius(-10.0)

def test_negative_kelvin_fahrenheit():
    with pytest.raises(ValueError):
        kelvin_to_fahrenheit(-10.0)

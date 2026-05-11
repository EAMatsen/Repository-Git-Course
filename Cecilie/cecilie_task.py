"""
Cecilie - Exercise: Convert Celsius to Fahrenheit

Goal:
- Complete the function to convert a Celsius temperature to Fahrenheit.
- Formula: Fahrenheit = (Celsius * 9 / 5) + 32
"""


def celsius_to_fahrenheit(celsius):
    Farenheit = (celsius * 9 / 5) + 32
    return Farenheit


# Test case for Cecilie
value = 0
print("Expected: 32")
print("Actual:", celsius_to_fahrenheit(value))

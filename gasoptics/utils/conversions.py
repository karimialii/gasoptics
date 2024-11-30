def convert_temperature(value, from_unit, to_unit):
    """Convert temperature between Celsius, Kelvin, and Fahrenheit."""
    if from_unit == "C" and to_unit == "K":
        return value + 273.15
    elif from_unit == "K" and to_unit == "C":
        return value - 273.15
    elif from_unit == "C" and to_unit == "F":
        return (value * 9/5) + 32
    elif from_unit == "F" and to_unit == "C":
        return (value - 32) * 5/9
    else:
        raise ValueError("Unsupported temperature conversion.")

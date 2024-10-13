def convert(fromUnit: str, toUnit: str, value: float) -> float:
    
    conversions = {
        "celsius": {
            "kelvin": lambda x: x + 273.15,
            "fahrenheit": lambda x: (x * 9/5) + 32,
        },
        "fahrenheit": {
            "celsius": lambda x: (x - 32) * 5/9,
            "kelvin": lambda x: (x - 32) * 5/9 + 273.15,
        },
        "kelvin": {
            "celsius": lambda x: x - 273.15,
            "fahrenheit": lambda x: (x - 273.15) * 9/5 + 32,
        },
        "miles": {
            "yards": lambda x: x * 1760,
            "meters": lambda x: x * 1609.34,
        },
        "yards": {
            "miles": lambda x: x / 1760,
            "meters": lambda x: x * 0.9144,
        },
        "meters": {
            "miles": lambda x: x / 1609.34,
            "yards": lambda x: x / 0.9144,
        }
    }

    
    if fromUnit not in conversions or toUnit not in conversions[fromUnit]:
        raise ValueError(f"Conversion from {fromUnit} to {toUnit} is not supported.")

    
    return conversions[fromUnit][toUnit](value)

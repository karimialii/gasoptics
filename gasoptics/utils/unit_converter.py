class UnitConverter:
    def __init__(self):
        # Conversion factors relative to SI units
        self.conversion_factors = {
            "T": {
                "K": lambda x: x,  # Kelvin remains the same
                "C": lambda x: x + 273.15,  # Celsius to Kelvin
                "F": lambda x: (x - 32) * 5 / 9 + 273.15,  # Fahrenheit to Kelvin
            },
            "p": {"Pa": 1, "bar": 1e5, "psi": 6894.76},  # Pressure
            "rho": {"kg/m³": 1, "g/cm³": 1000},  # Density
            "s": {"J/K": 1, "kJ/K": 1000},  # Entropy
            "h": {"J": 1, "kJ": 1000},  # Enthalpy
            "k": {"W/m·K": 1, "mW/m·K": 0.001},  # Thermal conductivity
            "mu": {"Pa·s": 1, "mPa·s": 0.001},  # Viscosity
        }
        self.default_units = {
            "T": "K",  # Temperature
            "p": "Pa",  # Pressure
            "rho": "kg/m³",  # Density
            "s": "J/K",  # Entropy
            "h": "J",  # Enthalpy
            "k": "W/m·K",  # Thermal conductivity
            "mu": "Pa·s",  # Viscosity
        }

    def set_default_units(self, **units):
        """
        Update the default units globally.
        :param units: Keyword arguments with new units (e.g., T="C", p="bar").
        """
        for key, unit in units.items():
            if key in self.default_units:
                self.default_units[key] = unit
            else:
                raise ValueError(f"Unsupported unit: {key}")

    def convert(self, value, from_unit, to_unit, category):
        """
        Converts a value from one unit to another within a specific category.

        :param value: Value to convert
        :param from_unit: Unit of the input value
        :param to_unit: Desired output unit
        :param category: Category of units (e.g., "T", "p", "h").
        :return: Converted value
        """
        if category not in self.conversion_factors:
            raise ValueError(f"Unsupported unit category: {category}")

        factors = self.conversion_factors[category]

        if from_unit not in factors or to_unit not in factors:
            raise ValueError(f"Unsupported units for category {category}: {from_unit} or {to_unit}")

        if callable(factors[from_unit]):
            value = factors[from_unit](value)
        else:
            value *= factors[from_unit]

        if callable(factors[to_unit]):
            return factors[to_unit](value)
        else:
            return value / factors[to_unit]

    def to_default_units(self, value, from_unit, category):
        """
        Converts a value to the default unit for a given category.

        :param value: Value to convert.
        :param from_unit: Unit of the input value.
        :param category: Category of units (e.g., "T", "p").
        :return: Value in default units.
        """
        to_unit = self.default_units[category]
        return self.convert(value, from_unit, to_unit, category)

    def from_default_units(self, value, to_unit, category):
        """
        Converts a value from the default unit to the desired unit for a given category.

        :param value: Value in default units.
        :param to_unit: Desired output unit.
        :param category: Category of units (e.g., "T", "p").
        :return: Value in the desired unit.
        """
        from_unit = self.default_units[category]
        return self.convert(value, from_unit, to_unit, category)

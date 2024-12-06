# utils/__init__.py

default_units = {
            "T": "K",  # Temperature
            "p": "Pa",  # Pressure
            "rho": "kg/m³",  # Density
            "s": "J/K",  # Entropy
            "h": "J",  # Enthalpy
            "k": "W/m·K",  # Thermal conductivity
            "mu": "Pa·s",  # Viscosity
        }

def set_default_units(**units):
    """
    Update the default units globally.
    :param units: Keyword arguments with new units.
    """
    for key, unit in units.items():
        if key in default_units:
            default_units[key] = unit
        else:
            raise ValueError(f"Unsupported unit: {key}")

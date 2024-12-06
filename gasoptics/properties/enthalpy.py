from .cp import calculate_cp
from .cv import calculate_cv
from .cv import calculate_humidity_ratio

def calculate_enthalpy(T, P, gas="air", RH=0):
    """
    Calculate the specific enthalpy (h) for a gas.

    - If gas is "air" and RH > 0, calculate for humid air.
    - If gas is "air" and RH = 0 (default), calculate for dry air.
    - For other gases, calculate real gas enthalpy.

    :param T: Temperature in Kelvin.
    :param P: Pressure in Pascals.
    :param gas: Name of the gas (default: "air").
    :param RH: Relative humidity (0 to 1, default: 0 for dry air).
    :return: Enthalpy (h) in J/kg.
    """
    if gas == "air" and RH > 0:  # Humid air case
        # Calculate the humidity ratio
        W = calculate_humidity_ratio(T, RH, P)

        # Specific heat capacities
        cp_dry_air = calculate_cp(T, P, gas="air")  # Dry air
        cp_water_vapor = calculate_cp(T, P, gas="water_vapor")  # Water vapor

        # Enthalpy calculation
        h_dry_air = cp_dry_air * T
        h_water_vapor = cp_water_vapor * T
        h_humid_air = h_dry_air + W * h_water_vapor
        return h_humid_air
    else:  # Dry air or any other gas
        # Calculate Cp
        cp = calculate_cp(T, P, gas=gas)
        # Enthalpy calculation
        h = cp * T
        return h

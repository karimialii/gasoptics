import math
from .cp import calculate_cp
from .cv import calculate_humidity_ratio
from .gas_constant import calculate_specific_gas_constant
from ..backends.redlich_kwong import calculate_redlich_kwong_Z

def calculate_entropy(T, P, gas="air", RH=0, reference_T=273.15):
    """
    Calculate the specific entropy (s) for a gas.

    - If gas is "air" and RH > 0, calculate for humid air.
    - If gas is "air" and RH = 0 (default), calculate for dry air.
    - For other gases, calculate real gas entropy.

    :param T: Temperature in Kelvin.
    :param P: Pressure in Pascals.
    :param gas: Name of the gas (default: "air").
    :param RH: Relative humidity (0 to 1, default: 0 for dry air).
    :param reference_T: Reference temperature in Kelvin (default: 273.15 K).
    :return: Entropy (s) in J/(kg·K).
    """
    if gas == "air" and RH > 0:  # Humid air case
        # Calculate the humidity ratio
        W = calculate_humidity_ratio(T, RH, P)

        # Specific entropy for dry air and water vapor
        cp_dry_air = calculate_cp(T, P, gas="air")  # Dry air
        cp_water_vapor = calculate_cp(T, P, gas="water_vapor")  # Water vapor

        s_dry_air = cp_dry_air * math.log(T / reference_T)
        s_water_vapor = cp_water_vapor * math.log(T / reference_T)

        # Real gas corrections
        Z_dry_air = calculate_redlich_kwong_Z(P, T, gas="air")
        Z_water_vapor = calculate_redlich_kwong_Z(P, T, gas="water_vapor")

        R_dry_air = calculate_specific_gas_constant("air")
        R_water_vapor = calculate_specific_gas_constant("water_vapor")

        s_real_dry_air = -R_dry_air * math.log(Z_dry_air)
        s_real_water_vapor = -R_water_vapor * math.log(Z_water_vapor)

        # Total entropy for humid air
        s_humid_air = (s_dry_air + s_real_dry_air) + W * (s_water_vapor + s_real_water_vapor)
        return s_humid_air
    else:  # Dry air or other gases
        # Calculate Cp
        cp = calculate_cp(T, P, gas=gas)

        # Ideal gas entropy
        s_ideal = cp * math.log(T / reference_T)

        # Real gas correction
        Z = calculate_redlich_kwong_Z(P, T, gas=gas)
        R_specific = calculate_specific_gas_constant(gas)
        s_real = -R_specific * math.log(Z)

        # Total entropy
        s = s_ideal + s_real
        return s

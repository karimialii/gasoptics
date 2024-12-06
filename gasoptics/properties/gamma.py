from .cp import calculate_cp
from .cv import calculate_cv

def calculate_gamma(T, P, gas="air", RH=0):
    """
    Calculate the ratio of specific heats (gamma = Cp / Cv) for a gas.

    - If gas is "air" and RH > 0, calculate for humid air.
    - If gas is "air" and RH = 0 (default), calculate for dry air.
    - For other gases, calculate for the real gas properties.

    :param T: Temperature in Kelvin.
    :param P: Pressure in Pascals.
    :param gas: Name of the gas (default: "air").
    :param RH: Relative humidity (0 to 1, default: 0 for dry air).
    :return: Gamma (dimensionless).
    """
    # Calculate Cp and Cv dynamically based on gas type and RH
    cp = calculate_cp(T, P, gas=gas, RH=RH)
    cv = calculate_cv(T, P, gas=gas, RH=RH)
    
    # Calculate and return gamma
    gamma = cp / cv
    return gamma

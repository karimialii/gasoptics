# state.py
# This module contains functions related to the state properties, specifically density
# for real gases, considering compressibility effects.

from .compressibility import calculate_compressibility_factor_with_C
from gasoptics.utils.constants import R_AIR

def calculate_real_gas_density(P, T):
    """
    Calculate the density of air considering real gas effects.

    :param P: Pressure in Pascals (Pa)
    :param T: Temperature in Kelvin (K)
    :return: Density in kg/m³
    """
    Z = calculate_compressibility_factor_with_C(P, T)
    return P / (Z * R_AIR * T)

# virial.py
# This module contains functions to calculate the compressibility factor using the Virial EOS.
# It calculates the second and third virial coefficients and computes the compressibility factor (Z).
from gasoptics.utils.constants import R_AIR
import numpy as np

def calculate_virial_coefficient_B(T):
    """
    Calculate the second virial coefficient (B) for a given temperature using empirical data.
    For air, we use a simplified formula. You can replace this with real data or more complex equations.

    :param T: Temperature in Kelvin (K)
    :return: Second virial coefficient B in m³/mol
    """
    # Example empirical data for air; replace with actual coefficients or more accurate models
    B = 3.18e-6 * T  # This is a simplified placeholder, actual data required for more accuracy
    return B

def calculate_virial_coefficient_C(T):
    """
    Calculate the third virial coefficient (C) for a given temperature using empirical data.
    For air, we use a simplified formula. You can replace this with real data or more complex equations.

    :param T: Temperature in Kelvin (K)
    :return: Third virial coefficient C in m³/mol·atm
    """
    # Example empirical data for air; replace with actual coefficients or more complex equations
    C = -2.10e-9 * T  # This is a simplified placeholder, actual data required for more accuracy
    return C

def calculate_compressibility_factor_with_C(P, T):
    """
    Calculate the compressibility factor (Z) using the Virial EOS.

    :param P: Pressure in Pascals (Pa)
    :param T: Temperature in Kelvin (K)
    :return: Compressibility factor (Z)
    """
    B = calculate_virial_coefficient_B(T)  # Get the second virial coefficient
    C = calculate_virial_coefficient_C(T)  # Get the third virial coefficient
    
    # Calculate the compressibility factor using the Virial equation
    Z = 1 + B * (P / (R_AIR * T)) + C * (P / (R_AIR * T))**2
    return Z

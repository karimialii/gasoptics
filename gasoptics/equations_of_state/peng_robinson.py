# peng_robinson.py
# This module contains functions for calculating properties of real gases using the Peng-Robinson EOS.
# It calculates the compressibility factor and density for real gases like air.

import numpy as np
from gasoptics.utils.constants import R_AIR

def calculate_peng_robinson_Z(P, T, T_c, P_c):
    """
    Calculate the compressibility factor Z using the Peng-Robinson EOS.

    :param P: Pressure in Pascals
    :param T: Temperature in Kelvin
    :param T_c: Critical temperature in Kelvin
    :param P_c: Critical pressure in Pascals
    :return: Compressibility factor Z
    """
    # Calculate parameters a and b based on the critical properties
    a = 0.45724 * (R_AIR**2 * T_c**2) / P_c
    b = 0.07780 * (R_AIR * T_c) / P_c
    A = a * P / (R_AIR**2 * T**2)
    B = b * P / (R_AIR * T)

    # Solve the cubic equation for the compressibility factor Z
    coeffs = [1, B - 1, A - 3 * B**2 - 2 * B, B**3 + B**2 - A * B]
    roots = [r.real for r in np.roots(coeffs) if r.imag == 0]
    return min(roots) if roots else None

def calculate_density_peng_robinson(P, T, T_c, P_c):
    """
    Calculate the density of air using the Peng-Robinson EOS.

    :param P: Pressure in Pascals
    :param T: Temperature in Kelvin
    :param T_c: Critical temperature in Kelvin
    :param P_c: Critical pressure in Pascals
    :return: Density in kg/m³
    """
    Z = calculate_peng_robinson_Z(P, T, T_c, P_c)
    if Z is None:
        raise ValueError("Failed to calculate Z-factor.")
    return P / (Z * R_AIR * T)

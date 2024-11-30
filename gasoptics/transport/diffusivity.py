# diffusivity.py
# This module contains functions for calculating gas diffusivity using the Chapman-Enskog equation.

import math

def calculate_gas_diffusivity(T, P, M, sigma, omega):
    """
    Calculate gas diffusivity using the Chapman-Enskog equation.

    :param T: Temperature in Kelvin
    :param P: Pressure in atm
    :param M: Reduced molecular weight in g/mol
    :param sigma: Lennard-Jones collision diameter in Ångstroms
    :param omega: Collision integral (dimensionless)
    :return: Diffusivity in cm²/s
    """
    return (0.001858 * T**1.5) / (P * math.sqrt(M) * sigma**2 * omega)

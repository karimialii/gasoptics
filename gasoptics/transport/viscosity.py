# viscosity.py
# This module contains functions for calculating dynamic viscosity for real gases.

def calculate_dynamic_viscosity(T):
    """
    Dynamic viscosity using Sutherland's law.

    :param T: Temperature in Kelvin
    :return: Dynamic viscosity in Pa·s
    """
    mu_ref = 1.716e-5  # Reference viscosity (Pa·s)
    T_ref = 273.15     # Reference temperature (K)
    S = 110.4          # Sutherland constant (K)
    return mu_ref * (T / T_ref)**1.5 * (T_ref + S) / (T + S)

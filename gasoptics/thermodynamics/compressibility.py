# compressibility.py
# This module contains functions related to the calculation of the compressibility factor (Z)
# using different equations of state (EOS), such as Virial EOS and Peng-Robinson EOS.

from gasoptics.utils.constants import R_AIR
from gasoptics.equations_of_state.virial import calculate_compressibility_factor_with_C  # Import from virial.py
from gasoptics.equations_of_state.peng_robinson import calculate_peng_robinson_Z  # Import from peng_robinson.py
from gasoptics.equations_of_state.virial import *
def calculate_compressibility_factor_virial(P, T):
    """
    Calculate the compressibility factor (Z) for a real gas using the Virial EOS.

    :param P: Pressure in Pascals (Pa)
    :param T: Temperature in Kelvin (K)
    :return: Compressibility factor (Z)
    """
    # Calculate Virial coefficients B and C for the given temperature
    B = calculate_virial_coefficient_B(T)
    C = calculate_virial_coefficient_C(T)
    
    # Compressibility factor (Z) calculation using the Virial EOS
    Z = 1 + B * (P / (R_AIR * T)) + C * (P / (R_AIR * T))**2
    return Z

def calculate_compressibility_factor_peng_robinson(P, T, T_c, P_c):
    """
    Calculate the compressibility factor (Z) for a real gas using the Peng-Robinson EOS.

    :param P: Pressure in Pascals (Pa)
    :param T: Temperature in Kelvin (K)
    :param T_c: Critical temperature in Kelvin (K)
    :param P_c: Critical pressure in Pascals (Pa)
    :return: Compressibility factor (Z)
    """
    # Calculate compressibility factor using the Peng-Robinson EOS
    Z = calculate_peng_robinson_Z(P, T, T_c, P_c)
    return Z

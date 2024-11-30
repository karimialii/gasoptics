
import numpy as np

def calculate_specific_heat_cp(T):
    """Calculate the specific heat capacity at constant pressure (C_p) and constant volume (C_v) for air."""
    # Constants for air
    A = 28.11
    B = 0.1967e-2
    C = 0.4802e-5
    D = -1.966e-9
    MW = 28.951  # molar mass of air in g/mol 

    # Formula for Cp in J/mol·K
    cp_molar = A + B * T + C * T**2 + D * T**3
    cp_mass = cp_molar*1000/MW
    return cp_mass

def calculate_specific_heat_cv(T):
    """Calculate specific heat capacity at constant volume (C_v) for air."""
    R = 287.05  # J/kg·K
    C_p = calculate_specific_heat_cp(T)
    return C_p - R

def calculate_gamma(T):
    """Calculate specific heat ratio γ = C_p / C_v."""
    C_p = calculate_specific_heat_cp(T)
    C_v = calculate_specific_heat_cv(T)
    return C_p / C_v


from gasoptics.thermodynamics.specific_heat import calculate_specific_heat_cp
import numpy as np

def calculate_enthalpy(T):
    """Calculate specific enthalpy for air."""
    C_p = calculate_specific_heat_cp(T)
    return C_p * T

def calculate_entropy(T, P, P_ref=101325):
    """Calculate specific entropy for air."""
    R = 287.05  # J/kg·K
    C_p = calculate_specific_heat_cp(T)
    return C_p * np.log(T) - R * np.log(P / P_ref)


from .enthalpy_entropy import calculate_enthalpy, calculate_entropy

def calculate_helmholtz_free_energy(T, P):
    """Calculate Helmholtz free energy for air."""
    u = calculate_enthalpy(T) - T * calculate_entropy(T, P)
    return u

def calculate_gibbs_free_energy(T, P):
    """Calculate Gibbs free energy for air."""
    h = calculate_enthalpy(T)
    s = calculate_entropy(T, P)
    return h - T * s

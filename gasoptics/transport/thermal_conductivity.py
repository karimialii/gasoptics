from gasoptics.transport.viscosity import calculate_dynamic_viscosity
from gasoptics.thermodynamics.specific_heat import calculate_specific_heat_cp
import numpy as np


def calculate_thermal_conductivity(T):
    """Calculate thermal conductivity for air."""
    C_p = calculate_specific_heat_cp(T)  # Calculate C_p if not provided
    Pr = 0.71 - 0.00001 * T
    mu = calculate_dynamic_viscosity(T)  # Get dynamic viscosity using the existing function
    return mu * C_p / Pr

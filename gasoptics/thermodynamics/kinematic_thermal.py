
from gasoptics.transport.viscosity import calculate_dynamic_viscosity
from gasoptics.transport.thermal_conductivity import calculate_thermal_conductivity
from .state import calculate_real_gas_density
from .specific_heat import calculate_specific_heat_cp

def calculate_kinematic_viscosity(T, P):
    """Calculate kinematic viscosity ν = μ / ρ."""
    mu = calculate_dynamic_viscosity(T)
    rho = calculate_real_gas_density(P, T)
    return mu / rho

def calculate_thermal_diffusivity(T, P):
    """Calculate thermal diffusivity α = λ / (ρ * C_p)."""
    lambda_ = calculate_thermal_conductivity(T)
    rho = calculate_real_gas_density(P, T)
    C_p = calculate_specific_heat_cp(T)
    return lambda_ / (rho * C_p)

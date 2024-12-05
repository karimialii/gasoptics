import math
from properties.gas_constant import load_gas_properties

def calculate_dynamic_viscosity(T, P=None, gas="air"):
    """
    Calculate the dynamic viscosity (mu) for a gas using Sutherland's law.

    - For low pressures: Sutherland's law is used.
    - For high pressures (if P is provided): Empirical correction is applied.

    :param T: Temperature in Kelvin.
    :param P: Pressure in Pascals (optional, for high-pressure correction).
    :param gas: Name of the gas (default: "air").
    :return: Dynamic viscosity (mu) in Pa·s.
    """
    # Load gas properties
    gas_properties = load_gas_properties(gas)

    # Extract Sutherland's constants
    if "sutherland_reference_temperature" in gas_properties and "sutherland_reference_viscosity" in gas_properties:
        T0 = gas_properties["sutherland_reference_temperature"]  # Reference temperature (K)
        mu0 = gas_properties["sutherland_reference_viscosity"]  # Reference viscosity (Pa·s)
        C = gas_properties["sutherland_constant"]  # Sutherland's constant (K)

        # Calculate viscosity using Sutherland's law
        mu = mu0 * ((T / T0) ** 1.5) * ((T0 + C) / (T + C))
    else:
        raise ValueError(f"Sutherland's constants not found for gas: {gas}")

    # Apply pressure correction if P is provided
    if P and "critical_pressure" in gas_properties and "pressure_correction_coefficient" in gas_properties:
        P_c = gas_properties["critical_pressure"]  # Critical pressure (Pa)
        alpha = gas_properties["pressure_correction_coefficient"]  # Pressure correction coefficient
        mu *= (1 + alpha * (P / P_c))

    return mu

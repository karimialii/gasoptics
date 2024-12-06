import math
from .gas_constant import load_gas_properties
from .cv import calculate_humidity_ratio
from ..backends.redlich_kwong import calculate_redlich_kwong_Z

def calculate_dynamic_viscosity(T, P=None, gas="air", RH=0):
    """
    Calculate the dynamic viscosity (mu) for a gas or humid air.

    - For dry air or other gases: Uses Sutherland's law.
    - For humid air (RH > 0): Accounts for water vapor using Wilke's mixing rule.

    :param T: Temperature in Kelvin.
    :param P: Pressure in Pascals (optional, for high-pressure correction).
    :param gas: Name of the gas (default: "air").
    :param RH: Relative Humidity (fraction between 0 and 1, default: 0 for dry air).
    :return: Dynamic viscosity (mu) in Pa·s.
    """
    if gas == "air" and RH > 0:  # Humid air case
        # Load properties for dry air and water vapor
        air_properties = load_gas_properties("air")
        water_vapor_properties = load_gas_properties("water_vapor")

        # Sutherland's law for dry air
        T0_air = air_properties["sutherland_vis_reference_temperature"]
        mu0_air = air_properties["sutherland_vis_reference"]
        C_air = air_properties["sutherland_vis_constant"]
        mu_air = mu0_air * ((T / T0_air) ** 1.5) * ((T0_air + C_air) / (T + C_air))

        # Sutherland's law for water vapor
        T0_vapor = water_vapor_properties["sutherland_vis_reference_temperature"]
        mu0_vapor = water_vapor_properties["sutherland_vis_reference"]
        C_vapor = water_vapor_properties["sutherland_vis_constant"]
        mu_vapor = mu0_vapor * ((T / T0_vapor) ** 1.5) * ((T0_vapor + C_vapor) / (T + C_vapor))

        # Saturation pressure of water vapor (Pa) using empirical formula
        T_celsius = T - 273.15
        P_vs = 611.21 * math.exp((17.502 * T_celsius) / (240.97 + T_celsius))  # Saturation vapor pressure in Pa
        P_v = RH * P_vs  # Partial pressure of water vapor
        P_d = P - P_v  # Partial pressure of dry air

        # Mole fractions
        x_vapor = P_v / P
        x_air = P_d / P

        # Wilke's mixing rule for dynamic viscosity
        mu_mix = mu_air * x_air + mu_vapor * x_vapor

        return mu_mix

    else:  # Dry air or other gases
        # Load gas properties
        gas_properties = load_gas_properties(gas)

        # Extract Sutherland's constants
        if "sutherland_vis_reference_temperature" in gas_properties and "sutherland_vis_reference" in gas_properties:
            T0 = gas_properties["sutherland_vis_reference_temperature"]
            mu0 = gas_properties["sutherland_vis_reference"]
            C = gas_properties["sutherland_vis_constant"]

            # Calculate viscosity using Sutherland's law
            mu = mu0 * ((T / T0) ** 1.5) * ((T0 + C) / (T + C))
        else:
            raise ValueError(f"Sutherland's constants not found for gas: {gas}")

        # Apply pressure correction if P is provided
        if P and "critical_pressure" in gas_properties and "pressure_correction_coefficient" in gas_properties:
            P_c = gas_properties["critical_pressure"]
            alpha = gas_properties["pressure_correction_coefficient"]
            mu *= (1 + alpha * (P / P_c))

        return mu

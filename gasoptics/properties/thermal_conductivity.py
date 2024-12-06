import math
from .gas_constant import load_gas_properties

def calculate_thermal_conductivity(T, P, gas="air", RH=0):
    """
    Calculate the thermal conductivity (lambda) for a gas or humid air.

    - For dry air or other gases: Uses Sutherland's law.
    - For humid air (RH > 0): Accounts for water vapor using a weighted mean or Wilke's rule.

    :param T: Temperature in Kelvin.
    :param P: Total pressure in Pascals.
    :param gas: Name of the base gas (default: "air").
    :param RH: Relative Humidity (fraction between 0 and 1, default: 0 for dry air).
    :return: Thermal conductivity (lambda) in W/m·K.
    """
    if gas == "air" and RH > 0:  # Humid air case
        # Load properties for dry air and water vapor
        air_properties = load_gas_properties("air")
        water_vapor_properties = load_gas_properties("water_vapor")

        # Sutherland's law for dry air
        T0_air = air_properties["sutherland_cond_reference_temperature"]
        lambda0_air = air_properties["sutherland_cond_reference"]
        C_air = air_properties["sutherland_cond_constant"]
        lambda_air = lambda0_air * ((T / T0_air) ** 1.5) * ((T0_air + C_air) / (T + C_air))

        # Sutherland's law for water vapor
        T0_vapor = water_vapor_properties["sutherland_cond_reference_temperature"]
        lambda0_vapor = water_vapor_properties["sutherland_cond_reference"]
        C_vapor = water_vapor_properties["sutherland_cond_constant"]
        lambda_vapor = lambda0_vapor * ((T / T0_vapor) ** 1.5) * ((T0_vapor + C_vapor) / (T + C_vapor))

        # Saturation pressure of water vapor (Pa)
        T_celsius = T - 273.15
        P_sat = 611.21 * math.exp((17.502 * T_celsius) / (240.97 + T_celsius))  # Saturation vapor pressure in Pa
        P_v = RH * P_sat  # Partial pressure of water vapor
        P_d = P - P_v  # Partial pressure of dry air

        # Mole fractions
        y_vapor = P_v / P
        y_air = P_d / P

        # Weighted arithmetic mean
        lambda_humid = y_air * lambda_air + y_vapor * lambda_vapor

        # Optional: Implement Wilke's mixing rule
        M_air = air_properties["molecular_weight"]
        M_vapor = water_vapor_properties["molecular_weight"]

        phi_air_vapor = ((1 + math.sqrt(lambda_air / lambda_vapor) * (M_vapor / M_air) ** 0.25) ** 2) / math.sqrt(
            8 * (1 + M_air / M_vapor)
        )
        phi_vapor_air = ((1 + math.sqrt(lambda_vapor / lambda_air) * (M_air / M_vapor) ** 0.25) ** 2) / math.sqrt(
            8 * (1 + M_vapor / M_air)
        )

        lambda_humid_wilke = (y_air * lambda_air / (y_air + y_vapor * phi_air_vapor)) + (
            y_vapor * lambda_vapor / (y_vapor + y_air * phi_vapor_air)
        )

        # Return thermal conductivity (weighted mean and Wilke's rule can be compared)
        return lambda_humid_wilke

    else:  # Dry air or other gases
        # Load gas properties
        gas_properties = load_gas_properties(gas)

        # Sutherland's law for thermal conductivity
        if "sutherland_cond_reference_temperature" in gas_properties and "sutherland_cond_reference" in gas_properties:
            T0 = gas_properties["sutherland_cond_reference_temperature"]
            lambda0 = gas_properties["sutherland_cond_reference"]
            C = gas_properties["sutherland_cond_constant"]

            # Calculate thermal conductivity using Sutherland's law
            lambda_gas = lambda0 * ((T / T0) ** 1.5) * ((T0 + C) / (T + C))
        else:
            raise ValueError(f"Sutherland's constants for thermal conductivity not found for gas: {gas}")

        return lambda_gas

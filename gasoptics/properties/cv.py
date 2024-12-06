import json
import os
import math
from ..backends.redlich_kwong import calculate_redlich_kwong_Z
from ..properties.cp import calculate_specific_heat_cp

# Path to the fluids folder containing gas-specific JSON files
FLUIDS_FOLDER = os.path.join(os.path.dirname(__file__), "..", "fluids")


def load_gas_properties(gas):
    """
    Load gas-specific properties from a JSON file in the fluids folder.

    :param gas: Name of the gas (e.g., "air").
    :return: Dictionary of gas properties.
    :raises FileNotFoundError: If the gas JSON file does not exist.
    """
    gas_file = os.path.join(FLUIDS_FOLDER, f"{gas}.json")
    if not os.path.isfile(gas_file):
        raise FileNotFoundError(f"Gas file '{gas}.json' not found in {FLUIDS_FOLDER}.")
    with open(gas_file, "r") as file:
        return json.load(file)


def calculate_real_gas_cv(T, P, gas):
    """
    Calculate specific heat capacity at constant volume (C_v) for a real gas.

    :param T: Temperature in Kelvin.
    :param P: Pressure in Pascals.
    :param gas: Name of the gas (must match a JSON file in the fluids folder).
    :return: C_v in J/(kg·K).
    """
    # Load gas properties
    gas_properties = load_gas_properties(gas)
    MW = gas_properties["molecular_weight"]  # Molar mass in g/mol
    R_specific = 8.314 / MW * 1000  # Specific gas constant in J/(kg·K)

    # Calculate ideal gas Cp and Cv
    cp_ideal = calculate_specific_heat_cp(T, gas=gas)
    cv_ideal = cp_ideal - R_specific

    # Compressibility factor Z using Redlich-Kwong EOS
    Z = calculate_redlich_kwong_Z(P, T, gas=gas)

    # Estimate d^2Z/dT^2 using finite differences
    dT = 1e-4  # Small temperature step
    Z_plus = calculate_redlich_kwong_Z(P, T + dT, gas=gas)
    Z_minus = calculate_redlich_kwong_Z(P, T - dT, gas=gas)
    d2Z_dT2 = (Z_plus - 2 * Z + Z_minus) / dT**2

    # Calculate real gas Cv
    cv_real = cv_ideal - T * d2Z_dT2 * R_specific
    return cv_real


def calculate_humidity_ratio(T, RH, P):
    """
    Calculate the humidity ratio (W) for humid air.

    :param T: Temperature in Kelvin.
    :param RH: Relative humidity (fraction, 0 to 1).
    :param P: Atmospheric pressure in Pascals.
    :return: Humidity ratio (W).
    """
    # Convert temperature to Celsius for saturation pressure calculation
    T_celsius = T - 273.15

    # Saturation pressure of water vapor (Pvs in Pascals)
    P_vs = 611.21 * math.exp((17.502 * T_celsius) / (240.97 + T_celsius))

    # Partial pressure of water vapor (Pv)
    P_v = RH * P_vs

    # Humidity ratio (W)
    W = 0.622 * (P_v / (P - P_v))
    return W


def calculate_cv(T, P, gas="air", RH=0):
    """
    Calculate specific heat capacity at constant volume (C_v) for a gas.

    - If gas is "air" and RH > 0, calculate for humid air.
    - If gas is "air" and RH = 0 (default), calculate for dry air.
    - For other gases, calculate real gas C_v.

    :param T: Temperature in Kelvin.
    :param P: Pressure in Pascals.
    :param gas: Name of the gas (default: "air").
    :param RH: Relative humidity (0 to 1, default: 0 for dry air).
    :return: C_v in J/(kg·K).
    """
    if gas == "air" and RH > 0:  # Humid air case
        W = calculate_humidity_ratio(T, RH, P)

        # Specific heat capacities at constant volume
        cv_dry_air = calculate_real_gas_cv(T, P, gas="air")  # Dry air
        cv_water_vapor = calculate_real_gas_cv(T, P, gas="water_vapor")  # Water vapor

        # Weighted average specific heat capacity
        cv_humid_air = cv_dry_air + W * cv_water_vapor
        return cv_humid_air
    else:  # Dry air or any other gas
        return calculate_real_gas_cv(T, P, gas)

import json
import os
import math
from backends.redlich_kwong import calculate_redlich_kwong_Z

# Path to the fluids folder containing gas-specific JSON files
FLUIDS_FOLDER = os.path.join(os.path.dirname(__file__), "..", "fluids")

def load_gas_constants(gas):
    """
    Load gas-specific constants from a JSON file in the fluids folder.

    :param gas: Name of the gas (e.g., "air").
    :return: Dictionary of gas constants.
    :raises FileNotFoundError: If the gas JSON file does not exist.
    """
    gas_file = os.path.join(FLUIDS_FOLDER, f"{gas}.json")
    if not os.path.isfile(gas_file):
        raise FileNotFoundError(f"Gas constants file for '{gas}' not found in {FLUIDS_FOLDER}.")
    
    with open(gas_file, "r") as file:
        return json.load(file)

def calculate_specific_heat_cp(T, gas="air"):
    """
    Calculate specific heat capacity at constant pressure (C_p) for a given gas.

    :param T: Temperature in Kelvin.
    :param gas: Name of the gas (must match a JSON file in the fluids folder).
    :return: C_p in J/(kg·K).
    """
    # Load gas-specific constants
    gas_constants = load_gas_constants(gas)
    A = gas_constants["specific_heats"]["A"]
    B = gas_constants["specific_heats"]["B"]
    C = gas_constants["specific_heats"]["C"]
    D = gas_constants["specific_heats"]["D"]
    MW = gas_constants["molecular_weight"]  # Molar mass in g/mol

    # Calculate molar Cp using the provided formula
    cp_molar = A + B * T + C * T**2 + D * T**3

    # Convert to mass-specific Cp (J/(kg·K))
    cp_mass = cp_molar * 1000 / MW
    return cp_mass

def calculate_real_gas_cp(T, P, gas="air"):
    """
    Calculate specific heat at constant pressure (C_p) for a real gas.

    :param T: Temperature in Kelvin.
    :param P: Pressure in Pascals.
    :param gas: Name of the gas (must match a JSON file in the fluids folder).
    :return: C_p in J/(kg·K).
    """
    # Load gas properties
    gas_properties = load_gas_constants(gas)
    MW = gas_properties["molecular_weight"]  # Molar mass in g/mol
    R_specific = 8.314 / MW * 1000  # Specific gas constant in J/(kg·K)

    # Ideal gas specific heat
    cp_ideal = calculate_specific_heat_cp(T, gas=gas)

    # Compressibility factor Z using Redlich-Kwong EOS
    Z = calculate_redlich_kwong_Z(P, T, gas=gas)

    # Estimate d^2Z/dT^2 using finite differences
    dT = 1e-4  # Small temperature step
    Z_plus = calculate_redlich_kwong_Z(P, T + dT, gas=gas)
    Z_minus = calculate_redlich_kwong_Z(P, T - dT, gas=gas)
    d2Z_dT2 = (Z_plus - 2 * Z + Z_minus) / dT**2

    # Calculate real gas specific heat
    cp_real = cp_ideal + T * d2Z_dT2 * R_specific
    return cp_real


def calculate_cp(T, P, gas="air", RH=0):
    """
    Calculate specific heat capacity at constant pressure (C_p) for a gas.

    - If gas is "air" and RH > 0, calculate for humid air.
    - If gas is "air" and RH = 0 (default), calculate for dry air.
    - For other gases, calculate real gas C_p.

    :param T: Temperature in Kelvin.
    :param P: Pressure in Pascals.
    :param gas: Name of the gas (default: "air").
    :param RH: Relative humidity (0 to 1, default: 0 for dry air).
    :return: C_p in J/(kg·K).
    """
    if gas == "air" and RH > 0:  # Humid air case
        # Convert temperature to Celsius for saturation pressure calculation
        T_celsius = T - 273.15

        # Saturation pressure of water vapor (Pvs in Pascals)
        P_vs = 611.21 * math.exp((17.502 * T_celsius) / (240.97 + T_celsius))

        # Partial pressure of water vapor (Pv)
        P_v = RH * P_vs

        # Humidity ratio (W)
        W = 0.622 * (P_v / (P - P_v))

        # Specific heat capacities
        cp_dry_air = calculate_real_gas_cp(T, P, gas="air")  # Dry air
        cp_water_vapor = calculate_specific_heat_cp(T, gas="water_vapor")  # Water vapor

        # Weighted average specific heat capacity
        cp_humid_air = cp_dry_air + W * cp_water_vapor
        return cp_humid_air
    else:  # Dry air or other gases
        # Load gas properties
        gas_constants = load_gas_constants(gas)
        A = gas_constants["specific_heats"]["A"]
        B = gas_constants["specific_heats"]["B"]
        C = gas_constants["specific_heats"]["C"]
        D = gas_constants["specific_heats"]["D"]
        MW = gas_constants["molecular_weight"]  # Molar mass in g/mol

        # Calculate molar Cp using the provided formula
        cp_molar = A + B * T + C * T**2 + D * T**3

        # Convert to mass-specific Cp (J/(kg·K))
        cp_mass = cp_molar * 1000 / MW

        # Real gas correction
        Z = calculate_redlich_kwong_Z(P, T, gas=gas)

        # Estimate d^2Z/dT^2 using finite differences
        dT = 1e-4  # Small temperature step
        Z_plus = calculate_redlich_kwong_Z(P, T + dT, gas=gas)
        Z_minus = calculate_redlich_kwong_Z(P, T - dT, gas=gas)
        d2Z_dT2 = (Z_plus - 2 * Z + Z_minus) / dT**2

        R_specific = 8.314 / MW * 1000  # Specific gas constant in J/(kg·K)
        cp_real = cp_mass + T * d2Z_dT2 * R_specific
        return cp_real

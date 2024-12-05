import math
import numpy as np
import json
import os

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

def calculate_redlich_kwong_Z(P, T, gas="air"):
    """
    Calculate the compressibility factor Z using the Redlich-Kwong EOS.

    :param P: Pressure in Pascals (Pa).
    :param T: Temperature in Kelvin (K).
    :param gas: Name of the gas (must match a JSON file in the fluids folder).
    :return: Compressibility factor Z (dimensionless).
    """
    # Universal gas constant (J/(mol·K))
    R = 8.314

    # Load gas-specific constants
    gas_constants = load_gas_constants(gas)
    T_c = gas_constants["critical_temperature"]
    P_c = gas_constants["critical_pressure"]

    # Calculate a and b for the gas
    a = 0.42748 * R**2 * T_c**2.5 / P_c
    b = 0.08664 * R * T_c / P_c

    # Calculate A and B
    A = a * P / (R**2 * T**2.5)
    B = b * P / (R * T)

    # Coefficients of the cubic equation for Z
    coeffs = [1, -1, A - B - B**2, -A * B]

    # Solve the cubic equation for Z
    roots = np.roots(coeffs)
    real_roots = [r.real for r in roots if r.imag == 0]

    # Return the smallest positive root (physical Z)
    Z = min(real_roots) if real_roots else None
    return Z

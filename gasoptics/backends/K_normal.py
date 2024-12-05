import math
import numpy as np
import json
import os
from .redlich_kwong import calculate_redlich_kwong_Z

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
    
def calculate_K_to_normal(T, p):
    """
    Calculate the normalized compressibility factor K1 using the specified EOS method.

    :param p: Pressure in Pascals
    :param T: Temperature in Kelvin
    :param p_c: Critical pressure in Pascals
    :param T_c: Critical temperature in Kelvin
    :param method: EOS method to use ("virial", "peng_robinson", or "redlich_kwong")
    :return: Normalized compressibility factor (K1)
    """
    # Calculate Z at the given pressure and temperature
    Z = calculate_redlich_kwong_Z(p, T)
    # Calculate Z1 at reference conditions (p=101325 Pa, T=0°C or 273.15 K)
    Z1 = calculate_redlich_kwong_Z(101325, 273.15)
    # Return normalized Z factor
    return round(Z / Z1, 4)

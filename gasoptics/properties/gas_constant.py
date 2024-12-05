import json
import os

# Path to the fluids folder
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

def calculate_specific_gas_constant(gas="air"):
    """
    Calculate the specific gas constant (R_specific) for a gas.

    :param gas: Name of the gas (default: "air").
    :return: Specific gas constant (R_specific) in J/(kg·K).
    """
    gas_properties = load_gas_properties(gas)
    MW = gas_properties["molecular_weight"]  # Molar mass in g/mol
    MW_kg = MW / 1000  # Convert to kg/mol
    R = 8.314  # Universal gas constant in J/(mol·K)
    R_specific = R / MW_kg
    return R_specific

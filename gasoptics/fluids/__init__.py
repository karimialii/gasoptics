import os
import json

# Path to the current folder
current_dir = os.path.dirname(__file__)

# Load fluid data dynamically from JSON files
fluid_data = {}
for file in os.listdir(current_dir):
    if file.endswith(".json"):
        with open(os.path.join(current_dir, file), 'r') as f:
            fluid_name = file.replace('.json', '')
            fluid_data[fluid_name] = json.load(f)

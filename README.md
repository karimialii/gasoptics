# Gasoptics

Gasoptics is a Python library for calculating thermodynamic and transport properties of gases, now updated to include enhanced functionality for real gas behavior, humid air modeling, and more robust computational methods.

## What's New in Version 2.0

- **Humid Air Modeling**: Added functions to calculate thermodynamic properties (e.g., \( C_p \), \( C_v \), and density) for humid air, including relative humidity considerations.
- **Enhanced Dynamic Viscosity**: Improved viscosity calculations using Sutherland’s law and empirical pressure corrections for high-pressure conditions.
- **Real Gas Handling**: Extended support for real gas properties using Redlich-Kwong and Peng-Robinson equations of state.
- **Improved Testing**: Expanded test coverage and added comparison with reference datasets.
- **Refactored Codebase**: Organized functions into specific modules for easier maintenance and scalability.
- **New Property Calculations**:
  - Specific Heat (\( C_p \), \( C_v \))
  - Ratio of Specific Heats (\( \gamma \))
  - Density
  - Dynamic Viscosity
  - Entropy and Enthalpy for real and ideal gases

## Features

- **Thermodynamic Properties**:
  - Specific heat (\( C_p, C_v \)), enthalpy, entropy, and \(\gamma\) for real and humid air.
- **Transport Properties**:
  - Viscosity and thermal conductivity calculations using empirical and theoretical models.
- **Equations of State**:
  - Support for Redlich-Kwong and Peng-Robinson EOS.
- **Modular Design**:
  - Organized codebase with dedicated modules for each property.
- **Utility Functions**:
  - Helper functions for handling gas constants and property lookups.

## Installation

### Option 1: Install from PyPI
```bash
pip install gasoptics
```

### Option 2: Install from Source
1. Clone the repository:
   ```bash
   git clone https://github.com/karimialii/gasoptics.git
   ```
2. Navigate into the project directory:
   ```bash
   cd gasoptics
   ```
3. Install the package:
   ```bash
   pip install .
   ```

## Requirements

- Python 3.x
- NumPy
- Matplotlib

## Usage

### Example: Calculating Thermodynamic Properties
```python
from gasoptics.thermodynamics import calculate_cp, calculate_cv, calculate_gamma
from gasoptics.transport import calculate_dynamic_viscosity

# Define conditions
T = 300  # Temperature in Kelvin
P = 101325  # Pressure in Pascals
RH = 0.5  # Relative Humidity (50%)

# Calculate specific heat at constant pressure
cp = calculate_cp(T, P, RH=RH)
print(f"Specific Heat (Cp): {cp} J/kg·K")

# Calculate specific heat at constant volume
cv = calculate_cv(T, P, RH=RH)
print(f"Specific Heat (Cv): {cv} J/kg·K")

# Calculate ratio of specific heats (gamma)
gamma = calculate_gamma(T, P, RH=RH)
print(f"Gamma (Cp/Cv): {gamma}")

# Calculate dynamic viscosity
mu = calculate_dynamic_viscosity(T, P)
print(f"Dynamic Viscosity: {mu} Pa·s")
```

### Example: Calculating Density
```python
from gasoptics.thermodynamics import calculate_density

# Conditions
T = 300  # Kelvin
P = 101325  # Pascals
RH = 0.8  # Relative Humidity (80%)

# Calculate density for humid air
rho = calculate_density(T, P, RH=RH)
print(f"Density of Humid Air: {rho:.3f} kg/m³")
```

## Tests

Run the test suite to validate functionality:
```bash
pytest tests/
```

## Contributing

Contributions are welcome! Follow these steps to contribute:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Make your changes and commit:
   ```bash
   git commit -am "Add new feature"
   ```
4. Push to your branch:
   ```bash
   git push origin feature/your-feature
   ```
5. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

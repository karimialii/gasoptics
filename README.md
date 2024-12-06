---

# GasOptics

GasOptics is a Python library designed to calculate thermodynamic and transport properties of gases. With the introduction of the `GasProperties` class, the library now provides a streamlined interface for handling various gas properties under different conditions, along with robust unit conversion capabilities.

---

## What's New in Version 0.3.0

- **The `GasProperties` Class**:
  - Unified interface for calculating gas properties.
  - Dynamic updates to conditions without reinitialization.
  - Support for unit conversions using `UnitConverter`.
- **Thermal Conductivity Calculations**:
  - Added support for thermal conductivity (`λ`) calculations for gases and humid air.
- **Enhanced Unit Handling**:
  - Seamless input and output unit conversion for temperature, pressure, enthalpy, and more.
- **Refactored Codebase**:
  - Modularized structure for easier maintenance and extensibility.

---

## Features

### The `GasProperties` Class
- **Dynamic Property Calculations**:
  - Specific Heat: \( C_p, C_v \)
  - Density: \( \rho \)
  - Dynamic Viscosity: \( \mu \)
  - Enthalpy: \( h \)
  - Entropy: \( s \)
  - Heat Capacity Ratio: \( \gamma \)
  - Thermal Conductivity: \( \lambda \)
- **Update Conditions Dynamically**:
  - Change temperature, pressure, or relative humidity without reinitialization.
- **Unit Conversion**:
  - Flexible input and output unit handling for consistent results.

---

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

---

## Requirements

- Python 3.x
- NumPy

---

## Usage

### Using `GasProperties`

The `GasProperties` class provides a convenient interface to calculate various thermodynamic and transport properties of gases.

#### Example 1: Basic Usage
```python
from gasoptics.properties import GasProperties

# Set global units
GasProperties.set_unit(T="C", p="bar", h="kJ")

# Create a GasProperties instance
props = GasProperties(T=25, p=1, RH=0.5, T_unit="C")  # 25°C, 1 bar, 50% RH

# Calculate properties
cp = props.cp()
rho = props.rho()
mu = props.mu()

print(f"Specific Heat (cp): {cp:.2f} kJ/kg·K")
print(f"Density (rho): {rho:.3f} kg/m³")
print(f"Viscosity (mu): {mu:.6f} Pa·s")
```

#### Example 2: Dynamic Updates
```python
# Update conditions dynamically
props.update_conditions(T=30, p=1.5, RH=0.6, T_unit="C")

# Recalculate properties
cp_updated = props.cp()
rho_updated = props.rho()

print(f"Updated Specific Heat (cp): {cp_updated:.2f} kJ/kg·K")
print(f"Updated Density (rho): {rho_updated:.3f} kg/m³")
```

---

## Available Methods in `GasProperties`

| Method  | Description                              |
|---------|------------------------------------------|
| `cp()`  | Specific heat at constant pressure (\( C_p \)). |
| `cv()`  | Specific heat at constant volume (\( C_v \)).  |
| `rho()` | Density (\( \rho \)).                    |
| `h()`   | Enthalpy (\( h \)).                      |
| `s()`   | Entropy (\( s \)).                       |
| `gamma()` | Heat capacity ratio (\( \gamma \)).     |
| `k()`   | Thermal conductivity (\( \lambda \)).    |
| `mu()`  | Dynamic viscosity (\( \mu \)).           |

---

## Tests

Run the test suite to validate functionality:
```bash
pytest tests/
```

---

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

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
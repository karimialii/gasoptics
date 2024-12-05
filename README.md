# Gasoptics

Gasoptics is a Python library for calculating thermodynamic and transport properties of gases. It includes functions for calculating specific heat, viscosity, thermal conductivity, and other properties using both ideal and real gas models.

## Features

- **Thermodynamics**: Includes functions for calculating specific heat, enthalpy, entropy, and more.
- **Transport Properties**: Includes functions for calculating viscosity, thermal conductivity, and kinematic viscosity.
- **Equations of State**: Includes Peng-Robinson and other equations for gas density calculations.
- **Utility Functions**: Helper functions for various thermodynamic and transport property calculations.

## Installation

To install **Gasoptics**, you can clone the repository or install it directly from a source distribution.

### Option 1: Install from source

1. Clone the repository:

   ```bash
   git clone https://github.com/karimialii/gasoptics.git
   ```

2. Navigate into the project directory:

   ```bash
   cd gasoptics
   ```

3. Install the package using pip:

   ```bash
   pip install .
   ```

### Option 2: Install via PyPI

You can install the package via pip:

```bash
pip install gasoptics
```

## Requirements

- Python 3.x
- NumPy

## Usage

Here’s an example of how to use the library to calculate thermodynamic and transport properties:

```python
from gasoptics import calculate_specific_heat_cp, calculate_dynamic_viscosity, calculate_thermal_conductivity

# Define temperature in Kelvin
T = 300  # K

# Calculate specific heat at constant pressure (Cp)
Cp = calculate_specific_heat_cp(T)
print(f"Specific Heat at Constant Pressure (Cp): {Cp} J/kg·K")

# Calculate dynamic viscosity
mu = calculate_dynamic_viscosity(T)
print(f"Dynamic Viscosity: {mu} Pa·s")

# Calculate thermal conductivity
k = calculate_thermal_conductivity(T)
print(f"Thermal Conductivity: {k} W/m·K")
```

## Tests

The package includes tests for all the core functions to ensure correctness. To run the tests, use the following command:

```bash
pytest tests/
```

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests for any improvements or bug fixes.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit (`git commit -am 'Add new feature'`).
4. Push to your branch (`git push origin feature/your-feature`).
5. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


### How to Use:
1. **Clone the Repository**: You can clone the repository using the provided `git clone` command.
2. **Install Dependencies**: Make sure you have NumPy installed.
3. **Usage Example**: The README includes an example for using the library's functions for calculating properties like specific heat, viscosity, and thermal conductivity.
4. **Running Tests**: Run tests using `pytest` to ensure that the library works as expected.
5. **Contributing**: The contributing section provides instructions for how others can contribute to the project.

This README will serve as a guide for anyone looking to use or contribute to the `gasoptics` library.

Let me know if you need any modifications!

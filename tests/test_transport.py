# tests/test_transport.py
import pytest
from gasoptics.transport import calculate_dynamic_viscosity, calculate_thermal_conductivity

def test_calculate_dynamic_viscosity():
    T = 300  # Temperature in Kelvin
    viscosity = calculate_dynamic_viscosity(T)
    assert viscosity > 0, f"Dynamic viscosity should be positive, got {viscosity}"

def test_calculate_thermal_conductivity():
    T = 300  # Temperature in Kelvin
    thermal_conductivity = calculate_thermal_conductivity(T)
    assert thermal_conductivity > 0, f"Thermal conductivity should be positive, got {thermal_conductivity}"

# tests/test_equations_of_state.py
import pytest
from gasoptics.equations_of_state import calculate_density_peng_robinson

def test_calculate_density_peng_robinson():
    P = 101325  # Pressure in Pascals
    T = 300  # Temperature in Kelvin
    density = calculate_density_peng_robinson(P, T, T_c=132.5, P_c=37.3 * 101325)
    assert density > 0, f"Density should be positive, got {density}"

# tests/test_thermodynamics.py
import pytest
from gasoptics.thermodynamics import calculate_specific_heat_cp, calculate_specific_heat_cv, calculate_enthalpy, calculate_entropy

def test_calculate_specific_heat_cp():
    T = 300  # Temperature in Kelvin
    cp = calculate_specific_heat_cp(T)
    assert cp > 0, f"Specific heat at constant pressure (Cp) should be positive, got {cp}"

def test_calculate_specific_heat_cv():
    T = 300  # Temperature in Kelvin
    cv = calculate_specific_heat_cv(T)
    assert cv > 0, f"Specific heat at constant volume (Cv) should be positive, got {cv}"

def test_calculate_enthalpy():
    T = 300  # Temperature in Kelvin
    enthalpy = calculate_enthalpy(T)
    assert enthalpy > 0, f"Enthalpy should be positive, got {enthalpy}"

def test_calculate_entropy():
    T = 300  # Temperature in Kelvin
    P = 101325  # Pressure in Pascals
    entropy = calculate_entropy(T, P)
    assert entropy > 0, f"Entropy should be positive, got {entropy}"

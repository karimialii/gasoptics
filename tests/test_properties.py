import unittest
from gasoptics.properties import (
    calculate_cp,
    calculate_cv,
    calculate_density,
    calculate_enthalpy,
    calculate_entropy,
    calculate_gamma,
    calculate_specific_gas_constant,
    calculate_dynamic_viscosity
)


class TestGasOpticsPackage(unittest.TestCase):

    def test_calculate_cp(self):
        """Test calculate_cp for air at standard conditions."""
        result = calculate_cp(T=300, P=101325, gas="air")
        self.assertAlmostEqual(result, 1005, delta=5)

    def test_calculate_cv(self):
        """Test calculate_cv for air at standard conditions."""
        result = calculate_cv(T=300, P=101325, gas="air")
        self.assertAlmostEqual(result, 718, delta=5)

    def test_calculate_density(self):
        """Test calculate_density for air at standard conditions."""
        result = calculate_density(T=300, P=101325, gas="air")
        self.assertAlmostEqual(result, 1.2, delta=0.1)

    def test_calculate_enthalpy(self):
        """Test calculate_enthalpy for air at standard conditions."""
        result = calculate_enthalpy(T=300, P=101325, gas="air")
        self.assertAlmostEqual(result, 301323.84, delta=2000)

    def test_calculate_entropy(self):
        """Test calculate_entropy for air at standard conditions."""
        result = calculate_entropy(T=300, P=101325, gas="air")
        self.assertAlmostEqual(result, 94.31, delta=0.5)

    def test_calculate_gamma(self):
        """Test calculate_gamma for air at standard conditions."""
        result = calculate_gamma(T=300, P=101325, gas="air")
        self.assertAlmostEqual(result, 1.4, delta=0.05)

    def test_calculate_specific_gas_constant(self):
        """Test calculate_specific_gas_constant for air."""
        result = calculate_specific_gas_constant(gas="air")
        self.assertAlmostEqual(result, 287, delta=1)

    def test_calculate_dynamic_viscosity(self):
        """Test calculate_dynamic_viscosity for air at standard conditions."""
        result = calculate_dynamic_viscosity(T=300, gas="air")
        self.assertAlmostEqual(result, 1.85e-5, delta=1e-6)


if __name__ == "__main__":
    unittest.main()

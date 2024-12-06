import sys
import os
import unittest

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from gasoptics.properties import GasProperties


class TestGasProperties(unittest.TestCase):
    def setUp(self):
        # Initialize a default GasProperties instance for tests
        self.gas_props = GasProperties(T=300, gas="air", p=101325, RH=0.5)

    def test_dynamic_viscosity(self):
        result = self.gas_props.mu()
        self.assertAlmostEqual(result, 1.8706659530502396e-05, places=6)

    def test_specific_heat_cp(self):
        result = self.gas_props.cp()
        self.assertAlmostEqual(result, 1025.0431, places=2)

    def test_specific_heat_cv(self):
        result = self.gas_props.cv()
        self.assertAlmostEqual(result, 717.2685, places=2)

    def test_density(self):
        result = self.gas_props.rho()
        self.assertAlmostEqual(result, 1.177, places=3)

    def test_enthalpy(self):
        result = self.gas_props.h()
        self.assertAlmostEqual(result, 301323.8397, places=2)

    def test_entropy(self):
        result = self.gas_props.s()
        self.assertAlmostEqual(result, 94.3064, places=1)

    def test_gamma(self):
        result = self.gas_props.gamma()
        self.assertAlmostEqual(result, 1.4, places=1)

    def test_gas_constant(self):
        result = self.gas_props.R()
        self.assertAlmostEqual(result, 287.1749, places=3)

    def test_update_conditions(self):
        # Update conditions and test
        self.gas_props.update_conditions(T=350, p=200000, RH=0.3)
        result_cp = self.gas_props.cp()
        result_mu = self.gas_props.mu()
        self.assertGreater(result_cp, 1000)  # Expect cp to increase with temperature
        self.assertGreater(result_mu, 1.8706659530502396e-05)  # Expect viscosity to increase


if __name__ == "__main__":
    unittest.main()

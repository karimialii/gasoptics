from .cp import calculate_cp
from .cv import calculate_cv
from .density import calculate_density
from .enthalpy import calculate_enthalpy
from .entropy import calculate_entropy
from .gamma import calculate_gamma
from .gas_constant import calculate_specific_gas_constant
from .thermal_conductivity import calculate_thermal_conductivity
from .viscosity import calculate_dynamic_viscosity
from ..utils.unit_converter import UnitConverter


class GasProperties:
    """
    Class to calculate various thermodynamic and transport properties for a gas.
    """

    unit_converter = UnitConverter()

    @classmethod
    def set_unit(cls, **units):
        """
        Set the global units for input and output parameters.

        :param units: Keyword arguments for unit settings (e.g., T="C", p="bar").
        """
        cls.unit_converter.set_default_units(**units)

    def __init__(self, T, gas="air", p=101325, RH=0, T_unit=None):
        """
        Initialize with temperature, optional gas, pressure, and relative humidity.

        :param T: Temperature (required).
        :param gas: Name of the gas (default: "air").
        :param p: Pressure in Pascals (default: 101325 Pa, 1 atm).
        :param RH: Relative humidity as a fraction (0 to 1, default: 0 for dry air).
        :param T_unit: Unit of the input temperature (e.g., "C", "K"). If None, uses default.
        """
        self.gas = gas
        self.p = p
        self.RH = RH

        # Convert temperature to default units and store
        T_unit = T_unit or self.unit_converter.default_units["T"]
        self.T = self.unit_converter.to_default_units(T, T_unit, "T")

    def update_conditions(self, T=None, p=None, RH=None, T_unit=None):
        """
        Update the temperature, pressure, and/or relative humidity for calculations.

        :param T: New temperature value (optional).
        :param p: New pressure value (optional).
        :param RH: New relative humidity (optional).
        :param T_unit: Unit of the new temperature (optional, default is global unit).
        """
        if T is not None:
            T_unit = T_unit or self.unit_converter.default_units["T"]
            self.T = self.unit_converter.to_default_units(T, T_unit, "T")
        if p is not None:
            self.p = p
        if RH is not None:
            self.RH = RH

    def cp(self):
        cp_value = calculate_cp(self.T, P=self.p, gas=self.gas, RH=self.RH)
        return self.unit_converter.from_default_units(cp_value, self.unit_converter.default_units["h"], "h")

    def cv(self):
        cv_value = calculate_cv(self.T, P=self.p, gas=self.gas, RH=self.RH)
        return self.unit_converter.from_default_units(cv_value, self.unit_converter.default_units["h"], "h")

    def rho(self):
        rho_value = calculate_density(self.T, P=self.p, gas=self.gas, RH=self.RH)
        return rho_value  # Density is returned in default units (kg/m³).

    def h(self):
        h_value = calculate_enthalpy(self.T, P=self.p, gas=self.gas, RH=self.RH)
        return self.unit_converter.from_default_units(h_value, self.unit_converter.default_units["h"], "h")

    def s(self):
        s_value = calculate_entropy(self.T, P=self.p, gas=self.gas, RH=self.RH)
        return self.unit_converter.from_default_units(s_value, self.unit_converter.default_units["s"], "s")

    def gamma(self):
        return calculate_gamma(self.T, P=self.p, gas=self.gas, RH=self.RH)

    def R(self):
        return calculate_specific_gas_constant(gas=self.gas)

    def k(self):
        k_value = calculate_thermal_conductivity(self.T, P=self.p, gas=self.gas, RH=self.RH)
        return k_value  # Thermal conductivity is returned in default units (W/m·K).

    def mu(self):
        mu_value = calculate_dynamic_viscosity(self.T, P=self.p, gas=self.gas, RH=self.RH)
        return mu_value  # Dynamic viscosity is returned in default units (Pa·s).

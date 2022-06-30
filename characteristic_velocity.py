import math

class CharacteristicVelocity:
    def __init__(self, specific_heat_ratio, gas_constant, temperature_at_nozzle_inlet):
        self.specific_heat_ratio = specific_heat_ratio
        self.gas_constant = gas_constant
        self.temperature_at_nozzle_inlet = temperature_at_nozzle_inlet

    def calculate(self):
        velocity = self.effective_velocity() / self.thrust_coeficiente()

        print("Characteristic velocity is %.2f m/s" % velocity)

    def effective_velocity(self):
        return math.sqrt(self.specific_heat_ratio * self.gas_constant * self.temperature_at_nozzle_inlet)

    def thrust_coeficiente(self):
        return self.specific_heat_ratio * math.sqrt((2 / (self.specific_heat_ratio + 1)) ** ((self.specific_heat_ratio + 1) / (self.specific_heat_ratio - 1)))


c_star = CharacteristicVelocity(1.2, 461, 4000)


c_star.calculate()
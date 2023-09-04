import math


class CapsulePressureVessel:
    def __init__(self, density: float, tensile_strength: float) -> None:
        self._density = density
        self._tensile_strength = tensile_strength

    def minimum_mass(self, pressure, radius, middle_cylinder_width) -> float:
        mass = 2 * math.pi * radius ** 2 * (radius + middle_cylinder_width) * pressure * (self._density / self._tensile_strength)

        return mass

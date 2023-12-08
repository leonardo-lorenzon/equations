import math


class CapsulePressureVessel:
    def __init__(self, density: float, tensile_strength: float) -> None:
        self._density = density
        self._tensile_strength = tensile_strength

    def volume(self, radius, middle_cylinder_width) -> float:
        cylinder_portion = math.pi * radius ** 2 * middle_cylinder_width

        sphere_portion = (4/3) * math.pi * radius ** 3

        return cylinder_portion + sphere_portion

    def area(self, radius, middle_cylinder_width) -> float:
        cylinder_portion = 2 * math.pi * radius * middle_cylinder_width

        sphere_portion = 4 * math.pi * radius ** 2

        return cylinder_portion + sphere_portion

    def average_thickness(self, pressure, radius, middle_cylinder_width) -> float:
        mass = self.minimum_mass(pressure, radius, middle_cylinder_width)

        area = self.area(radius, middle_cylinder_width)

        thickness = mass / (area * self._density)

        return thickness

    def minimum_mass(self, pressure, radius, middle_cylinder_width) -> float:
        mass = 2 * math.pi * radius ** 2 * (radius + middle_cylinder_width) * pressure * (self._density / self._tensile_strength)

        return mass


# Stainless steel 301 full hard: https://www.upmet.com/sites/default/files/datasheets/301-fh.pdf
stainless_301_full_hard = CapsulePressureVessel(7888, 1276000000)

print(f"Minimum mass: {stainless_301_full_hard.minimum_mass(3000000, 1.5, 12.15)}")
print(f"Volume: {stainless_301_full_hard.volume(1.5, 12.15)}")
print(f"Area: {stainless_301_full_hard.area(1.5, 12.15)}")
print(f"Average wall thickness: {stainless_301_full_hard.average_thickness(3000000, 1.5, 12.15)}")

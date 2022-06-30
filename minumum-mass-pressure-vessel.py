import math
def minumum_mass_sphere_pressure_vessel(pressure, radius, density, tensile_strength):
    volume = (4/3) * math.pi * radius**3

    mass = (3/2) * pressure * volume * (density / tensile_strength)

    print("Minumum mass for sphere pressure vessel %.2f Kg" % mass)


def minumum_mass_capsule_pressure_vessel(pressure, radius, middle_cilinder_width, density, tensile_strength):
    mass = 2 * math.pi * radius**2 * (radius + middle_cilinder_width) * pressure * (density / tensile_strength)

    print("Minumum mass for capsule pressure vessel %.2f Kg" % mass)


minumum_mass_sphere_pressure_vessel(15000000, 3.62, 1790, 7000000000)

minumum_mass_capsule_pressure_vessel(15000000, 3, 3, 1790, 7000000000)
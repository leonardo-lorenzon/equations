class Drag:
    def __init__(self, density, speed, drag_coefficient, area):
        self.density = density
        self.speed = speed
        self.drag_coefficient = drag_coefficient
        self.area = area

    def calculate_drag_force(self):
        force = (self.density * (self.speed ** 2) * self.drag_coefficient * self.area) / 2

        print("Drag force is %.2f N" % force)


drag = Drag(0.361133, 440, 0.55, 2.27)

drag.calculate_drag_force()
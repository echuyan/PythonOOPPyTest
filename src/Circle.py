from src.Figure import Figure
import math


class Circle(Figure):
    def __init__(self, radius, name):
        super().__init__(name)
        if radius <= 0:
            raise ValueError("Нельзя создать круг")
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius * self.radius

    def get_perimeter(self):
        return 2 * math.pi * self.radius

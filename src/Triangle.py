from Figure import Figure
import math


class Triangle(Figure):

    def __init__(self, side_a, side_b, side_c, name):
        super().__init__(name)
        if side_a <= 0 or side_b <= 0 or side_c <= 0 or \
                side_a+side_b <= side_c or side_b+side_c <= side_a or side_c\
                + side_a <= side_b:
            raise ValueError("Нельзя создать треугольник")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_area(self):
        half_perimeter = (self.side_a + self.side_b + self.side_c) / 2
        return math.sqrt(half_perimeter * (half_perimeter - self.side_a) *
                         (half_perimeter - self.side_b) *
                         (half_perimeter - self.side_c))

    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c

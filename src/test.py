from Square import Square
from Triangle import Triangle
from Rectangle import Rectangle
from Circle import Circle

# check square
square = Square(10, "square1")  # Так создаем квадрат со стороной 10
print(square.get_area())  # 100
print(square.get_perimeter())  # 40
# failed_square = Square(-10, "square2")

# check triangle
# Создаем треугольник со сторонами 13, 14, 15
triangle = Triangle(13, 14, 15, "tr1")
print(triangle.get_area())  # 84
print(triangle.get_perimeter())  # 42
# failed_triangle = Triangle(1, 1, 2, "tr2")

# check circle
circle = Circle(5, "circle1")
print(circle.get_area())  # 78.54
print(circle.get_perimeter())  # 31.42
# failed_circle = Circle(-10, "circle2")

# check rectangle
rectangle = Rectangle(5, 10, "rectangle1")
print(rectangle.get_area())  # 50
print(rectangle.get_perimeter())  # 30
# failed_rec = Rectangle(-10, -20, "rec2")

# add_area check
print(triangle.add_area(square))  # 184
print(circle.add_area(triangle))  # 162.54
print(rectangle.add_area(circle))  # 128.54
print(square.add_area(rectangle))  # 150

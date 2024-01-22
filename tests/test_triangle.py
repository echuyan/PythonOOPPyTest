import pytest
from src.Triangle import Triangle


@pytest.mark.parametrize("value", ["int", "float"], ids=["int", "float"])
def test_triangle_area_positive(get_triangle, value):
    """Testing triangle with int and float sides values, positive test"""
    a, b, c, name, area, perimeter = get_triangle(value=value)
    t = Triangle(a, b, c, name)
    assert t.get_area() == area


@pytest.mark.parametrize("value", ["int", "float"], ids=["int", "float"])
def test_triangle_perimeter_positive(get_triangle, value):
    """Testing triangle with int and float sides values, positive test"""
    a, b, c, name, area, perimeter = get_triangle(value=value)
    t = Triangle(a, b, c, name)
    assert t.get_perimeter() == perimeter


def test_triangle_negative_sides():
    """Testing triangle, negative test with negative sides values"""
    with pytest.raises(ValueError):
        Triangle(-5, 4, 7, "Negative")


def test_triangle_illegal_triangle():
    """Testing triangle according to the triangle inequality theorem"""
    with pytest.raises(ValueError):
        Triangle(1, 1, 2, "Negative")

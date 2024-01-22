import pytest
from src.Rectangle import Rectangle


def test_rectangle_area_positive(get_rectangle):
    """Testing rectangle with int and float sides values, positive test"""
    a, b, name, area, perimeter = get_rectangle
    r = Rectangle(a, b, name)
    assert r.get_area() == area


def test_rectangle_perimeter_positive(get_rectangle):
    """Testing rectangle with int and float sides values, positive test"""
    a, b, name, area, perimeter = get_rectangle
    r = Rectangle(a, b, name)
    assert r.get_perimeter() == perimeter


def test_rectangle_negative():
    """Testing rectangle, negative test with negative sides values"""
    with pytest.raises(ValueError):
        Rectangle(-5, -4, "Negative")

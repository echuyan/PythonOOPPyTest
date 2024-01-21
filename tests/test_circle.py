import pytest
from src.Circle import Circle


def test_circle_area_positive(get_circle):
    """Testing circle with int and float sides values, positive test"""
    a, name, area, perimeter = get_circle
    r = Circle(a, name)
    assert r.get_area() == area


def test_circle_perimeter_positive(get_circle):
    """Testing circle with int and float sides values, positive test"""
    a, name, area, perimeter = get_circle
    r = Circle(a, name)
    assert r.get_perimeter() == perimeter


def test_circle_negative():
    """Testing circle, negative test with negative sides values"""
    with pytest.raises(ValueError):
        Circle(-5, "Negative")

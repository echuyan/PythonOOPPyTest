import pytest
from src.Square import Square


def test_square_area_positive(get_square):
    """Testing square with int and float sides values, positive test"""
    a, name, area, perimeter = get_square
    r = Square(a, name)
    assert r.get_area() == area


def test_square_perimeter_positive(get_square):
    """Testing square with int and float sides values, positive test"""
    a, name, area, perimeter = get_square
    r = Square(a, name)
    assert r.get_perimeter() == perimeter


def test_square_negative():
    """Testing square, negative test with negative sides values"""
    with pytest.raises(ValueError):
        Square(-5, "Negative")

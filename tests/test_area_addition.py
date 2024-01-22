from src.Triangle import Triangle
from src.Rectangle import Rectangle
from src.Circle import Circle
from src.Square import Square


def test_area_additon(get_sum):
    """Testing rectangle with int and float sides values, positive test"""
    s, name1, t1, t2, t3, name2, r, name3, r1, r2, name4, trsq, citr, reci, sqre = get_sum
    Sq = Square(s, name1)
    Tr = Triangle(t1, t2, t3, name2)
    Ci = Circle(r, name3)
    Re = Rectangle(r1, r2, name4)

    assert Tr.add_area(Sq) == trsq
    assert Ci.add_area(Tr) == citr
    assert Re.add_area(Ci) == reci
    assert Sq.add_area(Re) == sqre

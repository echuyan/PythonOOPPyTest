import pytest


@pytest.fixture(scope="function", params=[(3, 5, "first", 15, 16), (3.5, 5.5, "second", 19.25, 18)], ids=["int", "float"])
def get_rectangle(request):
    """Fixture for passing data to rectangle test"""
    yield request.param


@pytest.fixture(scope="function", params=[(10, "first", 100, 40), (10.5, "second", 110.25, 42)], ids=["int", "float"])
def get_square(request):
    """Fixture for passing data to square test"""
    yield request.param


@pytest.fixture(scope="function", params=[(5, "first", 78.53981633974483, 31.41592653589793), (10.5, "second", 346.36059005827474, 65.97344572538566)], ids=["int", "float"])
def get_circle(request):
    """Fixture for passing data to circle test"""
    yield request.param


@pytest.fixture(scope="function")
def get_triangle():
    """Fixture for passing data to triangle test"""
    def __wrapper(value: str):
        if value == "int":
            return 13, 14, 15, "Triangle int", 84, 42
        elif value == "float":
            return 13.5, 14.5, 15.15, "Triangle float", 88.9910755686174,  43.15
        else:
            raise AssertionError("Only int or float")
    yield __wrapper


@pytest.fixture(scope="function", params=[(10, "square", 13, 14, 15, "Triangle", 5, "Circle", 5, 10, "Rectangle", 184, 162.53981633974485, 128.53981633974485, 150)])
def get_sum(request):
    """Fixture for passing data to area additon test"""
    yield request.param

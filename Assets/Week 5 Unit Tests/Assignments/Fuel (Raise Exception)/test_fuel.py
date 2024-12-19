import pytest
from fuel import convert, gauge, TooBigError


# test errors
def test_TooBigError():
    with pytest.raises(TooBigError):
        convert("4/3")

def test_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_ValueError():
    with pytest.raises(ValueError):
        convert("cat/dog")




# test percents
def test_conversion():
    assert convert("3/4") == (3, 4)
    assert convert("2/4") == (2, 4)
    assert convert("1/4") == (1, 4)


def test_E():
    assert gauge(1) == "E"
    assert gauge(.99) == "E"
    assert gauge(.75) == "E"
    assert gauge(0) == "E"

def test_F():
    assert gauge(99) == "F"
    assert gauge(99.1) == "F"
    assert gauge(99.5) == "F"
    assert gauge(100) == "F"

def test_between():
    assert gauge(75) == "75%"
    assert gauge(95) == "95%"
    assert gauge(20) == "20%"
    assert gauge(2) == "2%"

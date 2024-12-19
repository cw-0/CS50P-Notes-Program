import pytest
from bank import value


def test_hello():
    assert value("HELLO") == 0
    assert value("hello") == 0
    assert value("hElLo") == 0
    assert value("Hello there! How may I assist you?") == 0


def test_h():
    assert value("Hi") == 20
    assert value("hey") == 20
    assert value("HAPPY Halloween!") == 20
    assert value("helllo") == 20



def test_other():
    assert value("Welcome in!") == 100
    assert value("Whats your name?") == 100
    assert value("1234") == 100





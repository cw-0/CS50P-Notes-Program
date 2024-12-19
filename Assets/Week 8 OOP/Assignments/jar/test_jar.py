from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0
    

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.cookies == 5

    with pytest.raises(ValueError):
        jar.deposit(15)

    with pytest.raises(ValueError):
        jar.deposit(-1)

def test_withdraw():
    jar = Jar()
    jar.deposit(6)
    jar.withdraw(3)
    assert jar.size == 3

    with pytest.raises(ValueError):
        jar.withdraw(5)

    with pytest.raises(ValueError):
        jar.withdraw(-2)


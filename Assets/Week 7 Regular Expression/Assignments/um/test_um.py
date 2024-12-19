import pytest
from um import count


def test_in_word():
    assert count("you um gonna finish that drum") == 1

def test_spaces():
    assert count(" um ") == 1

def test_caps():
    assert count("UM um Um uM") == 4
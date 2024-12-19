import pytest
from plates import is_valid


def test_start_letters():
    assert is_valid("AAAAAA") == True
    assert is_valid("22AAAA") == False
    assert is_valid("A22222") == False
    assert is_valid("2AAAAA") == False

def test_max_char():
    assert is_valid("AAAAAAA") == False # 7 characters
    assert is_valid("AAAAAA") == True # 6 characters
    assert is_valid("AAAAA") == True # 5 characters
    assert is_valid("AAAA") == True # 4 characters
    assert is_valid("AAA") == True # 3 characters
    assert is_valid("AA") == True # 2 characters
    assert is_valid("A") == False # 1 characters

def test_invalid_number():
    assert is_valid("AAA222") == True
    assert is_valid("AA2222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("AAA022") == False
    assert is_valid("22AAAA") == False

def test_invalid_char():
    assert is_valid("AAAA.") == False
    assert is_valid("AAA AA") == False
    assert is_valid("AAA!") == False
    assert is_valid("Money$") == False
    
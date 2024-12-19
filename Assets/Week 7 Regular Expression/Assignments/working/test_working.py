import pytest
from working import convert


def test_oclock():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    
    
def test_valid_time():
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"

def test_twelves():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"


def test_24():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

def test_invalid_time():
    with pytest.raises(ValueError):
        assert convert("9:60 AM to 5:60 PM") == ValueError
def test_wrong_hour():
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")

def test_wrong_minute():
    with pytest.raises(ValueError):
        convert("12:60 AM to 5 PM")


def test_time():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:30 AM to 5:45 PM") == "09:30 to 17:45"


def test_to():
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")


def test_format():
    with pytest.raises(ValueError):
        convert("9 to 5")
    with pytest.raises(ValueError):
        convert("17:00 to 9 PM")
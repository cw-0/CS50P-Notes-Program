import pytest
from twttr import shorten

def test_caps():
    assert shorten("TWITTER") == "TWTTR"

def test_lower():
    assert shorten("twitter") == "twttr"

def test_numbers():
    assert shorten("9/25/2003") == "9/25/2003"

def test_symbols():
    assert shorten(".!@#$%^&*()><?") == ".!@#$%^&*()><?"

def test_vowels_only():
    assert shorten("www.AEIOU.com") == "www..cm"
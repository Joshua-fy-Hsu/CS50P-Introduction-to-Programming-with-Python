import pytest

from twttr import shorten

def test_shorten():
    assert shorten("AEIOU") == ""
    assert shorten("aeiou") == ""
    assert shorten("Twitter") == "Twttr"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("CS50") == "CS50"
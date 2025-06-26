import pytest
from datetime import date, timedelta
from seasons import SeasonCalculator

def test_minutes_lived_one_year():
    one_year_ago = date.today() - timedelta(days=365)
    calc = SeasonCalculator(one_year_ago.isoformat())
    assert calc.minutes_lived() == 525600 or calc.minutes_lived() == 527040

def test_minutes_lived_two_years():
    two_years_ago = date.today() - timedelta(days=730)
    calc = SeasonCalculator(two_years_ago.isoformat())
    expected = 1051200
    assert abs(calc.minutes_lived() - expected) <= 1440

def test_in_words():
    test_date = (date.today() - timedelta(days=365))
    calc = SeasonCalculator(test_date.isoformat())
    words = calc.in_words()
    assert "thousand" in words.lower()

def test_invalid_date(monkeypatch):
    with pytest.raises(SystemExit):
        SeasonCalculator("not-a-date")

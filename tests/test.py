import pytest
from main import calculate_age


@pytest.mark.parametrize("test_input, expected", [
    ("1990-01-01", 34),
    ("1995-06-15", 29),
    ("2005-12-30", 18),
    ("2010-11-20", 13),
    ("2034-03-05", None),
    ("20-04-1999",
     "Неверный формат даты рождения. Используйте формат YYYY-MM-DD."),
    ("2040-01-01", None)
])
def test_calculate_age(test_input, expected):
    assert calculate_age(test_input) == expected

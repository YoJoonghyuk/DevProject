from tests.main import calculate_age
import os
import pycodestyle
import pytest

def test_calculate_age_correct():
    birthdate = "1990-01-01"
    assert calculate_age(birthdate) == 34

def test_calculate_age_future_date():
    birthdate = "2050-01-01"
    assert calculate_age(birthdate) is None

def test_calculate_age_incorrect_format():
    birthdate = "01-01-1990"
    assert calculate_age(birthdate) == "Неверный формат даты рождения. Используйте формат YYYY-MM-DD."

def test_pep8_conformance():
    style = pycodestyle.StyleGuide()
    result = style.check_files([os.path.abspath("main.py")])
    assert result.total_errors == 0, f"Найдено {result.total_errors} стилистических ошибок в файле app.py: {','.join([f'{error.lineno}:{error.text}' for error in result.messages])}"
import pytest
from src.library_fun import calculator
# Тесты для функции калькулятора
def test_calculator():
    assert calculator(5, 2, '+') == 7
    assert calculator(8, 3, '-') == 5
    assert calculator(4, 2, '*') == 8
    assert calculator(10, 5, '/') == 2
    with pytest.raises(ValueError):
        calculator(6, 0, '/')  # Тест на обработку деления на ноль
import pytest
from src.library_fun import fibonacci

# Тесты для функции определения чисел Фибоначчи
def test_fibonacci():
    assert fibonacci(0) == [0]
    assert fibonacci(5) == [0, 1, 1, 2, 3]
    assert fibonacci(8) == [0, 1, 1, 2, 3, 5, 8, 13]
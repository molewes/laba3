import pytest
from src.library_fun import bubble_sort
# Тесты для функции сортировки пузырьком
def test_bubble_sort():
    assert bubble_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 5]) == [1, 1, 2, 3, 4, 5, 5, 5, 6, 9]
    assert bubble_sort([-3, -5, -2, -1, -4]) == [-5, -4, -3, -2, -1]
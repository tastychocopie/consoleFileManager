import math
import pytest


# Тесты для функции filter()
def test_filter():
    # Фильтрация четных чисел
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    filtered = list(filter(lambda x: x % 2 == 0, numbers))
    assert filtered == [2, 4, 6, 8, 10]

    # Фильтрация непустых строк
    strings = ["hello", "", "world", "", "python", ""]
    filtered_str = list(filter(None, strings))
    assert filtered_str == ["hello", "world", "python"]

    # Фильтрация с помощью функции
    def is_positive(x):
        return x > 0

    nums = [-5, -3, 0, 2, 4, -1, 6]
    filtered_pos = list(filter(is_positive, nums))
    assert filtered_pos == [2, 4, 6]


# Тесты для функции map()
def test_map():
    # Умножение всех элементов на 2
    numbers = [1, 2, 3, 4, 5]
    doubled = list(map(lambda x: x * 2, numbers))
    assert doubled == [2, 4, 6, 8, 10]

    # Преобразование чисел в строки
    str_numbers = list(map(str, numbers))
    assert str_numbers == ["1", "2", "3", "4", "5"]

    # Применение нескольких функций
    def square(x):
        return x ** 2

    def add_one(x):
        return x + 1

    result = list(map(lambda x: add_one(square(x)), numbers))
    assert result == [2, 5, 10, 17, 26]


# Тесты для функции sorted()
def test_sorted():
    # Сортировка чисел
    numbers = [5, 2, 8, 1, 9, 3]
    assert sorted(numbers) == [1, 2, 3, 5, 8, 9]
    assert sorted(numbers, reverse=True) == [9, 8, 5, 3, 2, 1]

    # Сортировка строк
    words = ["banana", "apple", "cherry", "date"]
    assert sorted(words) == ["apple", "banana", "cherry", "date"]
    assert sorted(words, key=len) == ["date", "apple", "banana", "cherry"]

    # Сортировка с помощью пользовательской функции
    def last_letter(s):
        return s[-1]

    assert sorted(words, key=last_letter) == ["banana", "apple", "date", "cherry"]


# Тесты для функций из библиотеки math
def test_math_pi():
    assert math.isclose(math.pi, 3.141592653589793, rel_tol=1e-9)


def test_math_sqrt():
    assert math.sqrt(4) == 2.0
    assert math.isclose(math.sqrt(2), 1.4142135623730951, rel_tol=1e-9)
    assert math.sqrt(0) == 0.0
    with pytest.raises(ValueError):
        math.sqrt(-1)


def test_math_pow():
    assert math.pow(2, 3) == 8.0
    assert math.isclose(math.pow(2, 0.5), 1.4142135623730951, rel_tol=1e-9)
    assert math.pow(5, 0) == 1.0
    assert math.isclose(math.pow(4, -1), 0.25, rel_tol=1e-9)


def test_math_hypot():
    assert math.hypot(3, 4) == 5.0
    assert math.isclose(math.hypot(1, 1), 1.4142135623730951, rel_tol=1e-9)
    assert math.hypot(0, 0) == 0.0
    assert math.isclose(math.hypot(2.5, 3.5), 4.301162633521313, rel_tol=1e-9)
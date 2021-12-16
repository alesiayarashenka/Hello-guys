def test_one_plus_one ():
    assert 1 + 1 == 2

def test_one_plus_two ():
    a = 1
    b = 2
    c = 3
    assert a + b == c

import pytest

def test_divide_by_zero ():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0

    assert 'division by zero' in str(e.value)

import pytest

products = [
    (2, 4, 8),          #умножение положительных чисел
    (1, 99, 99),        #умножение на 1
    (0, 99, 0),         #умножение на 0
    (2, -4, -8),        #умножение положительного числа на отрицательное
    (-4, -3, 12),       #умножение двух отрицательных чисел
    (2.5, 6.7, 16.75)   #умножение дробных чисел
]

@pytest.mark.parametrize ('a, b, product', products)
def test_multiplication(a, b, product):
    assert a * b == product



import pytest

from src.fizz_buzz import fizz_buzz

@pytest.mark.parametrize('number, result_expected', [
    (0, 'fizzbuzz'),
    (1, '1'),
    (2, '2'),
    (3, 'fizz'),
    (5, 'buzz'),
    (6, 'fizz'),
    (10, 'buzz'),
    (12, 'fizz'),
    (15, 'fizzbuzz'),
    (16, '16'),
    (18, 'fizz'),
    (20, 'buzz'),
    (21, 'fizz'),
    (25, 'buzz'),
    (27, 'fizz'),
    (30, 'fizzbuzz'),
    (33, 'fizz'),
    (35, 'buzz'),
    (40, 'buzz'),
    (45, 'fizzbuzz'),
    (51, 'fizz'),
    (60, 'fizzbuzz'),
    (75, 'fizzbuzz'),
    (90, 'fizzbuzz'),
    (100, 'buzz'),
    (111, 'fizz'),
    (225, 'fizzbuzz'),
    (333, 'fizz'),
    (555, 'buzz'),
    (999, 'fizz'),
    (1500, 'fizzbuzz'),
    (2020, 'buzz'),
    (3033, 'fizz'),
    (5000, 'buzz'),
    (9000, 'fizzbuzz'),
])

def test_number_returns_result_expected(number, result_expected):
    actual_result = fizz_buzz(number)
    assert actual_result == result_expected


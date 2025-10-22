import pytest

from src.fizz_buzz import fizz_buzz

@pytest.mark.parametrize('number,result_expected', [(0,'fizzbuzz'),(1,'1'),(2,'2'),(3,'fizz'),(4, '4')
])
def test_number_returns_result_expected(number, result_expected):
    actual_result = fizz_buzz(number)
    assert actual_result == result_expected


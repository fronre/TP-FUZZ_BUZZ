from src.fizz_buzz import fizz_buzz

def test_number_zero_returns_fizz_buzz():
    assert fizz_buzz(0) == "FizzBuzz"

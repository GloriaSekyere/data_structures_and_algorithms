import pytest
from script.fibonacci import fibonacci


def test_fibonacci_zero():
    assert fibonacci(0) == 0


def test_fibonacci_one():
    assert fibonacci(1) == 1


def test_fibonacci_two():
    assert fibonacci(2) == 1


def test_fibonacci_three():
    assert fibonacci(3) == 2


def test_fibonacci_five():
    assert fibonacci(5) == 5


def test_fibonacci_ten():
    assert fibonacci(10) == 55


def test_fibonacci_negative():
    assert fibonacci(-5) == 0


def test_fibonacci_large():
    assert fibonacci(20) == 6765

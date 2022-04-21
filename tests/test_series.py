import pytest
from math_series.series import fibonacci, lucas, sum_series

def test_fibonacci_one():
  actual = fibonacci(0)
  expected = 0
  assert actual == expected

def test_fibonacci_two():
  actual = fibonacci(1)
  expected = 1
  assert actual == expected

def test_fibonacci_three():
  actual = fibonacci(2)
  expected = 1
  assert actual == expected

def test_fibonacci_four():
  actual = fibonacci(3)
  expected = 2
  assert actual == expected

def test_fibonacci_five():
  actual = fibonacci(8)
  expected = 21
  assert actual == expected

def test_lucas_one():
  actual = lucas(0)
  expected = 2
  assert actual == expected

def test_lucas_two():
  actual = lucas(1)
  expected = 1
  assert actual == expected

def test_lucas_three():
  actual = lucas(3)
  expected = 4
  assert actual == expected

def test_lucas_four():
  actual = lucas(7)
  expected = 29
  assert actual == expected

def test_sum_series_one():
  actual = sum_series(1)
  expected = 1
  assert actual == expected

def test_sum_series_two():
  actual = sum_series(4, 2, 1)
  expected = 7
  assert actual == expected

def test_sum_series_three():
  actual = sum_series(4)
  expected = 3
  assert actual == expected

def test_sum_series_four():
  actual = sum_series(7, 2, 1)
  expected = 29
  assert actual == expected

def test_sum_series_five():
  actual = sum_series(7)
  expected = 13
  assert actual == expected


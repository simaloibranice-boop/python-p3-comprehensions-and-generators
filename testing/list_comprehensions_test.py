import pytest
from lib.list_comprehensions import (
    square_numbers,
    get_even_numbers,
    flatten_matrix,
    uppercase_strings,
    squares_generator
)

def test_square_numbers():
    assert square_numbers([1, 2, 3]) == [1, 4, 9]

def test_get_even_numbers():
    assert get_even_numbers([1, 2, 3, 4, 5]) == [2, 4]

def test_flatten_matrix():
    assert flatten_matrix([[1, 2], [3, 4]]) == [1, 2, 3, 4]

def test_uppercase_strings():
    assert uppercase_strings(['a', 'b', 'c']) == ['A', 'B', 'C']

def test_squares_generator():
    assert list(squares_generator([1, 2, 3])) == [1, 4, 9]

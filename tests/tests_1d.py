"""
tests for lab_1d.py.
"""

import pytest
from labs.lab_1.lab_1d import two_sum


def test_two_sum_example():
    
    result = two_sum([2, 7, 11, 15], 9)
    assert sorted(result) == [0, 1]


def test_two_sum_negative_numbers():
    
    result = two_sum([3, 2, 4], 6)
    assert sorted(result) == [1, 2]


def test_two_sum_with_negatives():
    
    result = two_sum([-3, 4, 3, 90], 0)
    assert sorted(result) == [0, 2]





def test_two_sum_duplicates():
    result = two_sum([3, 3], 6)
    assert sorted(result) == [0, 1]


def test_two_sum_zero_target():
    
    result = two_sum([5, -5, 1], 0)
    assert sorted(result) == [0, 1]


if __name__ == "__main__":
    pytest.main()

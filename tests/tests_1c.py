"""
Contains tests for lab_1c.py.
"""

import pytest
from labs.lab_1.lab_1c import max_subarray_sum


def test_max_subarray_with_mixed_numbers():
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6


def test_max_subarray_all_positive():
    assert max_subarray_sum([1, 2, 3, 4, 5]) == 15


def test_max_subarray_all_negative():
    
    assert max_subarray_sum([-5, -2, -8, -1, -4]) == -1


def test_max_subarray_single_element():
    assert max_subarray_sum([5]) == 5
    assert max_subarray_sum([-3]) == -3


def test_max_subarray_two_elements():
    assert max_subarray_sum([1, 2]) == 3
    assert max_subarray_sum([-1, -2]) == -1


def test_max_subarray_with_zeros():
    
    assert max_subarray_sum([0, 0, 0]) == 0
    assert max_subarray_sum([-1, 0, -1]) == 0



if __name__ == "__main__":
    pytest.main()

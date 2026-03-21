import pytest
from labs.lab_1.lab_1c import max_subarray_sum


def test_max_subarray_sum():
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_subarray_sum([1]) == 1  # Test for single element
    assert max_subarray_sum([-1]) == -1  # Test for single negative element
    assert (
        max_subarray_sum([5, -2, 3]) == 6
    )  # Test for mixed positive and negative numbers
    assert (
        max_subarray_sum([-2, -3, -1, -10, -12]) == -1
    )  # Test for all negative numbers
    assert max_subarray_sum([0, -3, 5, -2]) == 5
    assert max_subarray_sum([1, 2, 3, 4]) == 10
    assert max_subarray_sum([-2, -1, -3, -4]) == -1
    assert max_subarray_sum([0, 0, 0, 0]) == 0
    assert max_subarray_sum([10, 10, -5, -20, 20, 30, -100]) == 50

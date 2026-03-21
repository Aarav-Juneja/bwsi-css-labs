import pytest
from labs.lab_1.lab_1d import two_sum


def test_two_sum():
    # Test case 1: Basic test case
    nums = [2, 7, 11, 15]
    target = 9
    assert two_sum(nums, target) == [0, 1]

    # Test case 2: Negative numbers
    nums = [-3, 4, 3, 90]
    target = 0
    assert two_sum(nums, target) == [0, 2]

    # Test case 3: Multiple pairs (should return the first valid pair)
    nums = [1, 2, 3, 4, 5]
    target = 5
    assert two_sum(nums, target) == [1, 2]

    # Test case 4: No solution (though the problem guarantees one exists)
    nums = [1, 2, 3]
    target = 7
    assert two_sum(nums, target) == []

from trainig.two_sum import Solution
import pytest


@pytest.mark.parametrize("Solution ,nums, target,expected_result", [(Solution,[2, 7, 11, 15], 9, [0, 1]),
                                                          (Solution, [2, 3, 3, 15], 6, [1, 2]),
                                                          (Solution, [1, 7, 4, 88], 89, [0, 3]),
                                                          (Solution, [2, 7, 33, 22], 55, [2, 3]),
                                                          (Solution, [2, 7, 11, 15], 13, [0, 2]),
                                                          (Solution, [3, 4, 5, 6], 7, [0, 1])])
def test_two_sum(Solution, nums, target, expected_result):
    assert Solution.twoSum(Solution, nums, target) == expected_result

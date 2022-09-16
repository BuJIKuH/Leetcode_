from trainig.add_two_numbers import Solution
import pytest


@pytest.mark.parametrize("Solution ,l1, l2 ,expected_result", [(Solution, [2, 4, 3], [5, 6, 4], [7, 0, 8]),
                                                          (Solution, [6, 4, 35], [3, 6, 44], [9, 0, 8, 9]),
                                                          (Solution, [1, 2, 5], [3, 6, 9], [4, 8, 4, 1])])

def test_add_two_numbers(Solution, l1, l2, expected_result):
    assert Solution.addTwoNumbers(Solution, l1, l2) == expected_result
import pytest

from trainig.search_inserp_positions import Solution


@pytest.mark.parametrize("Solution ,nums, target,expected_result", [(Solution, [2, 7, 11, 15], 7, 1),
                                                                    (Solution, [2, 3, 3, 15], 15, 3),
                                                                    (Solution, [1, 7, 4, 88], 1, 0),
                                                                    (Solution, [1, 5, 2, 6, 3, 7, 11, 34], 3, 4),
                                                                    (Solution, [1, 5, 2, 6, 3, 7, 11, 34], 11, 6),
                                                                    (Solution, [1, 5, 2, 6, 3, 7, 11, 34], 22, None)])
def test_binary_search(Solution, nums, target, expected_result):
    assert Solution.search_binary(Solution, nums, target) == expected_result

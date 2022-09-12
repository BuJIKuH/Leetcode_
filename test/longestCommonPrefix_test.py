from trainig.longest_common_prefix import Solution
import pytest


@pytest.mark.parametrize("Solution, strs, expected_result", [(Solution, ["fower","flow","fat"], 'f'),
                                                          (Solution, ["flower","flow","flat"], 'fl'),
                                                          (Solution, ["big","bowling","must"], ''),
                                                          (Solution, ['nexia', 'nemo', 'neo'], 'ne')])


def test_longestCommonPrefix(Solution, strs, expected_result):
    assert Solution.longestCommonPrefix(Solution, strs) == expected_result
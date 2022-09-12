import pytest

from trainig.valid_parantheses import Solution


@pytest.mark.parametrize("Solution, s, expected_result", [(Solution, ["[{([[[]]])()(){}}]"], True),
                                                          (Solution, ["]()(){}[[()]]"], False),
                                                          (Solution, ["[(sjd),""],{2:3}, []"], True),
                                                          (Solution, ['{[[[[((()))]]]]}'], False),
                                                          (Solution, ['(]'], False)])
def test_isvalid(Solution, s, expected_result):
    assert Solution.isValid(Solution, s) == expected_result

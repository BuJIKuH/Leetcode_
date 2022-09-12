from trainig.roman_to_integer import Solution
import pytest


@pytest.mark.parametrize("Solution, s, expected_result", [(Solution, 'V', 5),
                                                          (Solution, 'I', 1),
                                                          (Solution, 'XX', 20),
                                                          (Solution, 'VII', 7),
                                                          (Solution, 'MM', 2000),
                                                          (Solution, 'C', 100)])


def test_roman_to_integer(Solution, s, expected_result):
    assert Solution.romanToInt(Solution, s) == expected_result


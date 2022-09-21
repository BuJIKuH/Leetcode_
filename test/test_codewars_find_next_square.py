import pytest

from trainig.codewars_next_sqrt import find_next_square


@pytest.mark.parametrize(" n, expected_result", [(4, 9),
                                                (121, 144),
                                                (81, 100),
                                                (25, 36),
                                                (100, 121),
                                                (155, -1),
                                                (100, 121),
                                                 (342786627, -1)])


def test_find_next_square(n, expected_result):
    assert find_next_square(n) == expected_result
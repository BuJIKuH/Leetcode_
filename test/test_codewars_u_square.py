import pytest

from trainig.codewars_u_square import is_square


@pytest.mark.parametrize(" n, expected_result", [(4, True),
                                                (26, False),
                                                (25, True),
                                                (8, False),
                                                (0, True),
                                                (81, True)])


def test_is_square(n, expected_result):
    assert is_square(n) == expected_result

import pytest
from trainig.pallindrom import isPalindrome


@pytest.mark.parametrize(" x, expected_result", [(121, True),
                                                    (345544, False),
                                                    (345543, True),
                                                    (12345678987654321, True)])


def test_ispallindrome(x, expected_result):
    assert isPalindrome(x) == expected_result
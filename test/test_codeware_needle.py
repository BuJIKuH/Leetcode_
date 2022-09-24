import pytest

from trainig.codeware_neeadle import find_needle


@pytest.mark.parametrize(" n, expected_result", [(
["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"], 'found the needle at position [5]'),
(["hay", "junk", "hay", "hay", "moreJunk", "randomJunk", "needle"], 'found the needle at position [6]'),
(["hay", "junk", "hay", "hay",  "needle", "moreJunk","randomJunk"], 'found the needle at position [4]'),
(["hay", "junk", "needle", "hay", "hay", "moreJunk", "randomJunk"], 'found the needle at position [2]'),
(["hay", "junk", "hay", "hay", "moreJunk", "randomJunk"], None),

             ])


def test_find_needle(n, expected_result):
    assert find_needle(n) == expected_result
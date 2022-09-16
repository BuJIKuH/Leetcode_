import pytest
from trainig.merge_two_sorted_list import mergeTwoLists, selectionSort

@pytest.mark.parametrize(" list1, list2, expected_result",
                        [([43312, 123], [5473], ['1', '1', '2', '2', '3', '3', '3', '3', '4', '4', '5', '7']),
                        ([12347, 56], [998], ['1', '2', '3', '4', '5', '6', '7', '8', '9', '9']),
                        ([321], [546], ['1', '2', '3', '4', '5', '6']),
                        ([43312, 123], [5473, 3212343], ['1', '1', '1', '2', '2', '2', '2', '3', '3', '3', '3', '3', '3', '3', '4', '4', '4', '5', '7'])])

def test_merge_two_sorted_list(list1, list2, expected_result):
    assert selectionSort(mergeTwoLists(list1, list2)) == expected_result
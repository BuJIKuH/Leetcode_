from typing import Optional
from datetime import datetime


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
start = datetime.utcnow()
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:

        # if list1 is None:
        #     return list2
        # if list2 is None:
        #     return list1
        # res = []
        #
        # for i in list1:
        #     for j in str(i):
        #         res.append(j.strip(' ,{}'))
        # for i in list2:
        #     for j in str(i):
        #         res.append(j.strip(' ,{}'))
        #
        # def find_smallest(res: Optional[list]) -> int:
        #     smallest = res[0]
        #     smallest_index = 0
        #     for i in range(1, len(res)):
        #         if res[i] < smallest:
        #             smallest = res[i]
        #             smallest_index = i
        #
        #     return smallest_index
        #
        # def selectionSort(res: Optional[list]) -> Optional[list]:
        #     new_list = []
        #     for i in range(len(res)):
        #         smallest = find_smallest(res)
        #         new_list.append(res.pop(smallest))
        #     return new_list
        #
        # return selectionSort(res)

        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

print(Solution().mergeTwoLists([3211241124547457], [546123123123345345]))
# print(mergeTwoLists([321], [546]))
finish = start - datetime.utcnow()
print(finish)
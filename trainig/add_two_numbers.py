from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res1 = ''
        res2 = ''
        for i in str(l1):
            res1 += i.strip(',').strip('[]').strip()
        res1 = ''.join(reversed(res1))

        for i in str(l2):
            res2 += i.strip(',').strip('[]').strip()
        res2 = ''.join(reversed(res2))

        result = ''.join((reversed(str(int(res1) + int(res2)))))
        '''данное выражение для Leetcode'''
        # result1 = int(res1) + int(res2)
        # result2 = str(result1)
        # result3 = ''.join((reversed(result2)))

        finish_result = [int(item) for item in result]

        return finish_result


print(Solution.addTwoNumbers(Solution, [1, 2, 5], [3, 6, 6]))

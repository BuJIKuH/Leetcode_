from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {']': '[', ')': '(', '}': '{'}
        collects = deque()
        for i in s:
            if i in '[({':
                collects.append(i)
            if i in '])}':
                if len(collects):
                    i = brackets[i]
                    if i != collects.pop():
                        return False
                else:
                    return False
        if len(collects):
            return False
        return True

print(Solution.isValid(Solution,'[{([[[]]])()(){}}]'))
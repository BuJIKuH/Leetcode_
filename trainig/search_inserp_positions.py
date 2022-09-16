from typing import List


class Solution:
    def __init__(self, list, item):
        self.list = list
        self.item = item

    def search_binary(self, list: List[int], item: int) -> int:
        low = 0
        height = len(list) - 1

        while low <= height:
            mid = (low + height)
            guess = list[mid]
            if guess == item:
                return mid
            elif guess > item:
                height = mid - 1
            else:
                low = mid + 1
        return None
    #


print(Solution.search_binary(Solution, [1, 5, 2, 6, 3, 7, 11, 34], 3))
print(Solution.search_binary(Solution, [1, 1, 2, 6, 4, 7, 23, 43], 6))
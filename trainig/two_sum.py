from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Словарь для хранения разницы и ее индекса
        index_map = {}
        # Цикл для каждого элемента
        for i, n in enumerate(nums):
            # Разница, которую необходимо проверить
            difference = target - n
            if difference in index_map:
                return [index_map[difference], i]
            else:
                index_map[n] = i
        return


print(Solution.twoSum(Solution, [2, 7, 33, 22], 55))

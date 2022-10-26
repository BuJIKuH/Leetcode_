def incrementer(nums):
    return [(i + k) % 10 for i, k in enumerate(nums, 1)]


print(incrementer([4, 6, 7, 1, 3]))
print(incrementer([3, 6, 9, 8, 9]))
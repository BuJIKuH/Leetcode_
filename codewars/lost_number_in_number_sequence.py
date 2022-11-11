def find_deleted_number(arr, mixed_arr):
    return sum(arr) - sum(mixed_arr)


assert find_deleted_number([1, 2, 3, 4, 5], [3, 4, 1, 5]) == 2
assert find_deleted_number([1, 2, 3, 4, 5], [3, 4, 1, 5, 2]) == 0
assert find_deleted_number([1, 2, 3, 4, 5, 6, 7], [3, 4, 1, 5, 2, 6]) == 7

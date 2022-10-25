def reverse(lst):
    empty_list = list()
    cur = len(lst) - 1
    while 0 <= cur:
        empty_list.append(lst[cur])
        cur -= 1
    return empty_list


assert reverse([1, 2, 3]) == [3, 2, 1]
assert reverse([1, 2, 3, 4]) == [4, 3, 2, 1]
assert reverse([]) == []
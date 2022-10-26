
def reverse(lst):
    empty_list = list()
    cur = len(lst) - 1
    while 0 <= cur:
        empty_list.append(lst[cur])
        cur -= 1
    return empty_list


def up_array(arr):
    cur = len(arr) - 1
    time_one = 0
    result = []
    if len(arr) < 1:
        return None
    elif 9 < arr[len(arr) - 1]:
        return None
    elif 0 > arr[len(arr) - 1]:
        return None
    while 0 <= cur:

        if arr[cur] == 9:
            result.append(0)
            cur -= 1
            time_one += 1

        elif arr[cur] != 9 and cur == len(arr) - 1:
            result.append(arr[cur] + 1)
            cur -= 1

        elif arr[cur] == 0 and cur == len(arr) - 1:
            result.append(arr[cur] + 1)
            cur -= 1

        elif time_one == 1:
            result.append(arr[cur] + 1)
            time_one = 0
            cur -= 1
        else:
            result.append(arr[cur])
            cur -= 1
    if time_one > 1:
        result.append(1)

    return reverse(result)


assert up_array([4, 3, 2, 5]) == [4, 3, 2, 6]
assert up_array([1, 2, 3, 9]) == [1, 2, 4, 0]
assert up_array([9, 9, 9]) == [1, 0, 0, 0]
assert up_array([1, 0, 0, 0]) == [1, 0, 0, 1]
assert up_array([1, 0, 0, 33]) is None
assert up_array([1, 0, 0, -3]) is None

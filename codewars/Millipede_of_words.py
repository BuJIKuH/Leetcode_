def solution(arr):
    l, r = 0, 1
    last = len(arr) - 1

    while r <= last >= l:
        if arr[l][-1] == arr[r][0]:
            return True
        elif arr[l][-1] != arr[r][0]:
            r += 1
        elif r == last + 1:
            l += 1

    return False


assert solution(["excavate", "endure", "screen", "desire", "theater", "excess", "night"]), True
assert solution(["trade", "pole", "view", "grave", "ladder", "mushroom", "president"]) == False
assert solution(['endure', 'excavate', 'example', 'transport']), True
assert solution(['no', 'no', 'dragon', 'on']), True

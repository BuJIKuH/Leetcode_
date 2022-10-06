def find_outlier(integers):
    oddArr = []
    evenArr = []

    for i in integers:
        if i % 2 == 0:
            evenArr.append(i)
        else:
            oddArr.append(i)
    if len(oddArr) > len(evenArr):
        return evenArr[0]
    else:
        return oddArr[0]


assert find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]) == 11
assert find_outlier([160, 3, 1719, 19, 11, 13, -21]) == 160

from typing import Optional


def mergeTwoLists(list1: Optional[list],
                  list2: Optional[list]) -> Optional[list]:
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    res = []
    for i in list1:
        for j in str(i):
            res.append(j)
    for i in list2:
        for j in str(i):
            res.append(j)
    return res

def find_smallest(res):
    smallest = res[0]
    smallest_index = 0
    for i in range(1, len(res)):
        if res[i] < smallest:
            smallest = res[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


print(selectionSort(mergeTwoLists([321], [546])))




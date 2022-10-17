array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
# def snail(snail_map):
#
#     res = []
#     while len(array) > 0:
#         #  go right
#         res += array[0]
#         del array[0]
#
#         if len(array) > 0:
#             # go down
#             for i in array:
#                 res += [i[-1]]
#                 del i[-1]
#
#             if array[-1]:
#                 # go left
#                 res += array[-1][::-1]
#                 del array[-1]
#
#             # go top
#             for i in reversed(array):
#                 res += [i[0]]
#                 del i[0]
#     return res



def snail(array):
    out = []
    while len(array):
        out += array.pop(0)
        array = list(zip(*array))[::-1] # Rotate
    return out

print(snail(array))



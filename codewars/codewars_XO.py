def xo(s):
    count_x = 0
    count_o = 0
    x = ['x', 'X']
    o = ['o', 'O']
    for i in s:
        if i == x[0] or i == x[1]:
            count_x += 1
        if i == o[0] or i ==o[1]:
            count_o += 1
    if count_x == count_o or count_x == 0 and count_o == 0:
        return True
    else:
        return False


print(xo('zpzpzpo'))
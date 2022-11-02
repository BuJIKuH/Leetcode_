def validate(n):
    n = str(n)
    res = []
    if len(n) % 2 == 0:
        for i, k in enumerate(n):
            if i % 2 != 0:
                res.append(int(k))
            elif i % 2 == 0:
                res.append(int(k) * 2)

    elif len(n) % 2 != 0:
        for j, v in enumerate(n):
            if j % 2 != 0:
                res.append(int(v) * 2)
            elif j % 2 == 0:

                res.append(int(v))
    for q in res:
        if q > 9:
            res.remove(q)
            res.append(q - 9)

    if sum(res) % 10 != 0:
        return False
    else:
        return True


assert validate(1714) == False
assert validate(12345) == False
assert validate(2121) == True
assert validate(123) == False
assert validate(9705205816) == False

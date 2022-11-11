
def persistence(n):
    res = 1
    if n < 10:
        return 0
    for i in str(n):
        res *= int(i)

    return 1 + persistence(res)


# print(persistence(39))
print(persistence(999))
# assert persistence(39) == 3
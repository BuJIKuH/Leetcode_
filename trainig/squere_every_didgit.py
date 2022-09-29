def square_digits(nums):
    sqr = []
    for num in str(nums):
        s = str(int(num) ** 2)
        sqr.append(s)
    ans = ''.join(sqr)
    return int(ans)


print(square_digits(9119))
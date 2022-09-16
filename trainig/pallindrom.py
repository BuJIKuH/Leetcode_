def isPalindrome(x: int) -> bool:
    flag = False
    s = str(x)
    revers = ''.join(reversed(s))
    if s == revers:
        flag = True
        return flag
    return flag

print(isPalindrome(111333555))


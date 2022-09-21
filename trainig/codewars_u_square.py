

def is_square(n: int) -> int:
    root = n ** (0.5)
    if n == root ** 2 or n == 0:
        return True
    else:
        return False

print(is_square(0))
print(is_square(25))
print(is_square(16))
print(is_square(4))
print(is_square(26))
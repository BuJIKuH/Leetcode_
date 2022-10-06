

def find_next_square(n: int) -> int:
    root = round(n ** (0.5))
    if n == root ** 2 or n == 0:
        return int((root + 1) ** 2)
    else:
        return -1

print(find_next_square(100))
print(find_next_square(81))
print(find_next_square(121))
print(find_next_square(342786627))
print(find_next_square(155))
def sum_even_numbers(seq):
    l = 0
    res = 0
    while l <= len(seq) - 1:
        if seq[l] % 2 == 0:
            res += seq[l]
            l += 1

        else:
            l += 1

    return res

print(sum_even_numbers([4, 3, 1, 2, 5, 10, 6, 7, 9, 8]))
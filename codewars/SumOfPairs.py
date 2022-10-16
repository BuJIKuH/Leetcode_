def sum_pairs(ints, s):
    seen = {}
    for i, num in enumerate(ints):
        comp = s - num
        if comp in seen:
            ans = [num, seen[comp]]
            return ans[::-1]
        seen[num] = num


print(sum_pairs([1, 4, 8, 7, 3, 15], 8))

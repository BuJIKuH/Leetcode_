def get_count(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in sentence:
        if i in vowels:
            count += 1
    return count


assert get_count('aeiou') == 5
assert get_count('abracadabra') == 5
assert get_count('') == 0
assert get_count('mommy') == 1

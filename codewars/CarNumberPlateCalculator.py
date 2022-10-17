# letters =  abcdefghijklmnopqrstuvwxyz
import string

letters = list(string.ascii_lowercase)


def find_the_number_plate(n):
    digit = str(n % 999 + 1).rjust(3, '0')  # находим номер
    discharge = n // 999  # разрядность
    return letters[discharge % 26] \
           + letters[(discharge // 26) % 26] \
           + letters[(discharge // (26 * 26)) % 26] \
           + digit


print(find_the_number_plate(1001))

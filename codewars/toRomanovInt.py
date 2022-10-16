class RomanNumerals:

    def to_roman(num):
        roman_digit = [('I', 1),
                       ('V', 5),
                       ('X', 10),
                       ('L', 50),
                       ('C', 100),
                       ('D', 500),
                       ('M', 1000)]

        result = ''
        while num > 0:
            for i, digit in roman_digit[::-1]:
                while num >= digit:
                    if num == 9:
                        result += 'IX'
                        num -= 9
                    elif num == 4:
                        result += 'IV'
                        num -= 4
                    elif (num//10) * 10 == 40:
                        result += 'XL'
                        num -= 40
                    elif (num//100) * 100 == 400:
                        result += 'CD'
                        num -= 400
                    elif ((num // 10) * 10) == 90:
                        result += 'XC'
                        num -= 90

                    elif ((num // 100) * 100) == 900:
                        result += 'CM'
                        num -= 900
                    else:
                        result += i
                        num -= digit
        return result

    def from_roman(val):
        roman_digit = {'I': 1,
                       'V': 5,
                       'X': 10,
                       'L': 50,
                       'C': 100,
                       'D': 500,
                       'M': 1000}
        n = len(val) - 1
        result = roman_digit[val[n]]
        for i in range(n - 1, -1, -1):
            if roman_digit[val[i]] >= roman_digit[val[i + 1]]:
                result += roman_digit[val[i]]
            else:
                result -= roman_digit[val[i]]
        return result



print(RomanNumerals.to_roman(1990))
print(RomanNumerals.from_roman('MMXX'))


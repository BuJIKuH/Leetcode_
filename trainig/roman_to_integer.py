
class Solution:
    def romanToInt(self, roman: str) -> int:
        roman_digit = {'I': 1,
                       'V': 5,
                       'X': 10,
                       'L': 50,
                       'C': 100,
                       'D': 500,
                       'M': 1000}

        n = len(roman)
        result = roman_digit[roman[n - 1]]
        for i in range(n - 2, -1, -1):
            if roman_digit[roman[i]] >= roman_digit[roman[i + 1]]:
                result += roman_digit[roman[i]]
            else:
                result -= roman_digit[roman[i]]
        return result

print(Solution.romanToInt(Solution, 'CXVII'))



def to_camel_case(text):
    if len(text) == 0:
        return ''
    first = text[0]
    if first.isupper():
        return text.replace('-', ' ').replace('_', " ").title().replace(' ', '')
    else:
        return text[0] + text.replace('-', ' ').replace('_', " ").title().replace(' ', '')[1:]


print(to_camel_case("the-stealth-warrior"))
print(to_camel_case("The_Stealth_Warrior"))

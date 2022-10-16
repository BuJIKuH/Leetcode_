def strip_comments(strng, markers):
    res = ''
    for i in markers:
        match i:
            case '#':
                ''.join(strng.split('#')[0])

    return res




print(strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']))
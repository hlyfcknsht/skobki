import sys
s = sys.argv[1]


def brackets_check(s):
    meetings = 0
    for i in s:
        if i == '(':
            meetings += 1
        elif i == ')':
            meetings -= 1
            if meetings < 0:
                return print(0)
    if meetings > 0:
        return print(0)
    return print(1)


brackets_check(s)


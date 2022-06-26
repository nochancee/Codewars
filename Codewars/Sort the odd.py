from re import L


def solution(s):
    if len(s) == 0:
        return (list(s))
    elif len(s) == 1:
        s1 = []
        s1.append(s+_)
    else:
        for i in s:
            
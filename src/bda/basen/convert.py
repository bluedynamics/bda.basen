# -*- coding: utf-8 -*-


def str2int(number, ref):
    base = len(ref)
    res = 0
    for digit in number:
        res *= base
        res += ref.index(digit)
    return res


def int2str(number, ref):
    res = []
    while number > 0:
        res.append(ref[number % len(ref)])
        number /= len(ref)
    res.reverse()
    return "".join(res)

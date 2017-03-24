__author__ = 'Lynn'


def pnorm(v, p):
    s = 0
    for i in range(len(v)):
        s += v[i]**p
    val = s**(1/p)
    return val

print pnorm([1, 4], 2)



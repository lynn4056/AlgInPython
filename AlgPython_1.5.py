__author__ = 'Lynn'


def count(data, target):
    n = 0
    for item in data:
        if item == target:
            n += 1
    return n


def contains(data, target):
    for item in data:
        if item == target:
            return True
    return False

x = count((1, 2, 3, 3), 3)

y = contains((2, 4, 5), 8)

print(x, y)


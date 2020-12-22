from sys import argv


def function():
    a, b, c = map(int, argv[1::])
    return a * b + c


print(function())

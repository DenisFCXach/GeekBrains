from math import log, ceil

a = int(input())
b = int(input())
# n = 0
# while a < b:
#     a += a / 10
#     n += 1
# print(n + 1)

print(ceil(1 + log(b / a) / log(1.1)))

n = int(input())
b = 0
while n // 10 != 0:
    a = n % 10
    n = n // 10
    if a > b:
        b = a
print(b)
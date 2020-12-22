def fact():
    a, b = 1, int(input())
    if b == 0:
        yield f'{b}! = 1'
    for i in range(1, b + 1):
        a *= i
        yield f'{i}! = {a}'


for j in fact():
    print(j)

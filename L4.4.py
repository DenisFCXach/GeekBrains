def function():
    mas = []
    a = [int(input()) for i in range(int(input()))]
    for i in a:
        if i in mas:
            continue
        else:
            mas.append(i)
    return mas


print(function())

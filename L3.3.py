def function(a, b, c):
    mas = [a, b, c]
    mas.remove(min(mas))
    return sum(mas)


print(function(int(input()), int(input()), int(input())))

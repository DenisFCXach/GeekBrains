def function(a, b):
    while b == 0:
        b = float(input('Деление на ноль! Введите другое значение: '))
    return a / b


print(function(int(input()), int(input())))

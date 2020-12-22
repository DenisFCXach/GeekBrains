def my_func(x, y):
    while x < 0 or y > 0:
        print('Вы ввели неправильные значения!')
        x = int(input('Введите первое значение: '))
        y = int(input('Введите второе значение: '))
    a = 1
    for i in range(abs(y)):
        a *= x
    return 1 / a


print(my_func(float(input("Первое значение: ")), int(input("Второе значение: "))))


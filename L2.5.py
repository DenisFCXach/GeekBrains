a = [input('Введите число: ')]
b = ''
while b != 'нет':
    b = input('Хотите ли вы ввести еще число? ')
    if b == 'да':
        a.append(input('Введите число: '))
        a = sorted(a, reverse=True)
        print('Ваш текущий рейниг:', ", ".join(map(str, a)) + '.')
    if b == 'нет':
        break
print('Результат:', ", ".join(map(str, a)) + '.')
# спрашиваем, хотят ли ввести еще чисел. если да
# , то аппендим и сортируем по убываению (a = sorted(a, reverse=True))

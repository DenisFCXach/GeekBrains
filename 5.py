a = int(input("значение выручки: "))
b = int(input('издержки фирмы: '))
print('работает в ' + ('прибыль ' if a > b else 'убыль ') + f'на {abs(a - b)}')

s = int(input('количество сотрудников: '))
print('прибыль фирмы в расчете на одного сотрудника ', (a - b) / s)


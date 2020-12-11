n = int(input('Введите месяц: '))
d = {
    'зима': [12, 1, 2],
    'весна': [3, 4, 5],
    'лето': [6, 7, 8],
    'осень': [9, 10, 11]
}

for name, date in d.items():
    if n in date:
        print('время года:', name)

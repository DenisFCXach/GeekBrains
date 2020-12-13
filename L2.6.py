n = int(input("Введите количество товаров: "))
disk = []
for stick in range(n):
    disk.append((stick, {
        'название': input('Введите название: '),
        'цена': int(input('Введите цену товара: ')),
        'количество': int(input('Введите количество товара: ')),
        'ед': input('Единица измерений: ')
    }))

if disk:
    temp = [a[1] for a in disk]
    mapper = {}

    for stick in temp:
        for key in stick.keys():
            if key not in mapper.keys():
                mapper[key] = []
            if key == "ед" and stick[key] not in mapper[key] or key != "ед":
                mapper[key].append(stick[key])

    for i, j in mapper.items():
        print(f'"{i}": {j}')
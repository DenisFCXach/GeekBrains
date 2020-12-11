a = str(input('Введите строку: '))
a = a.split(' ')
print("\n".join([(str(i + 1) + ' ' + a[i][:10]) for i in range(len(a))]))

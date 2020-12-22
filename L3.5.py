def function():
    a = 0
    while True:
        num = input('Напишите "exit" чтобы закончить ввод. ')
        num = num.split()
        for i in num:
            if num == 'exit':
                return a
            else:
                try:
                    a += int(i)
                except ValueError:
                    print('чтобы выйти из программы, надонажать "exit"')
        print('сумма введенных чисел равна: ', a)


print(function())
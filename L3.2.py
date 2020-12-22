def function(name, female, year, city, email, number):
    print('Имя:', name, 'Фамилия:', female, 'Год рождения:', year, 'Город:', city, 'Email:', email,
          'Телефон:', number)


function(name=input('Введите имя: '), female=input('Введите фамилию: '),
         year=input('Введите год рождения: '), city=input('Введите город: '),
         email=input('Введите email: '), number=input('Введите номер телефона: '))

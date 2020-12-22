# def int_func():
#     a = str(input()).title()
#     return a
#
#
# print(int_func())

def int_func():
    a = str(input()).split(' ')
    b = []
    for i in a:
        b.append(i[0].upper() + i[1:])
    return ' '.join(b)


print(int_func())

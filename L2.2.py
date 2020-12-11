a = int(input('Количество элементов, которые вы хотите внести в массив: '))
A = [input() for i in range(a)]
for i in range(0, len(A) - 1, 2):
    A[i], A[i + 1] = A[i + 1], A[i]
# b = A[i]
# A[i] = A[i + 1]
# A[i + 1] = b
print(*A)

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и 
# последний элемент, второй и предпоследний и т.д.
#     Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random, math
b = abs(int(input('Введите число заначений:')))
a = [random.randint(0,10) for _ in range(b)]
print(a, '->',end=" ")
for i in range(len(a)):
    if i<len(a)/2:
        proizv=a[i]*a[b-1-i]
        print(proizv,',', end=" ")
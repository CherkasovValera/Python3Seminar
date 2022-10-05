    # Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#     Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
# import random, math
# b = abs(float(input('Введите число заначений:')))
# a = [random.randint(0,10) for _ in range(b)]
num = [1.1, 1.2, 3.1, 5, 10.01]
des = []
for i in range(5): 
    if num[i]%1 !=0:
        num[i]=num[i]-int(num[i])
        des.append(num[i])
        r = (max(des)-min(des))
print(round(r,5))

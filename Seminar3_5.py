#     Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

#     Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
# F(-n)=((-1)**n+1)*F(n)   или Fn=F(n+2)-F(n+1)


import math
b = abs(int(input('Введите число:')))
kod = []
for i in range(-b,b+1):
    kod.append(i)
for i in range(-b-2,-len(kod)-1,-1):
    kod[i]=kod[i+2]-kod[i+1]
for i in range(b+2,len(kod),1):
    kod[i]=kod[i-2]+kod[i-1]
print(kod)
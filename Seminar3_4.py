#     Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#     Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


import math
b = abs(int(input('Введите число заначений:')))
kod = []
print(b,' -> ',end='')
if b==0:
    print(b,end='')
else:
        while b>= 1:
            n=b%2
            b=b//2
            kod.append(n)
kod.reverse()
print(*kod,sep='')



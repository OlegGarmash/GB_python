'''
Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai .
Последняя строка содержит число X
5
1 2 3 4 5
6
-> 5
'''

import random

lenlst = int(input("Введите длину списка: "))
lst = []

for i in range(lenlst):
    lst.append(random.randint(1, 100))

print(lst)

x = int(input("Введите число X: "))

delta_i = 0
delta = x - lst[delta_i]
if delta < 0:
    delta *= -1

for i in range(len(lst)):
    delta_x = x - lst[i]
    if delta_x < 0:
        delta_x *= -1
    if delta_x < delta:
        delta_i = i
        delta = delta_x

print(f'Самый близкий по величине элемент, число: {lst[delta_i]}')
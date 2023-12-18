'''
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
Вводится список чисел.
Все числа списка находятся на разных строках.
'''

import random

lenlst = int(input('Введите длину списка N: '))
lst = [random.randint(0, 10) for _ in range(lenlst)]

print(lst)
setlst = set(lst)
doublelst = []
for item in setlst:
    count = 0
    for i in lst:
        if item == i:
            count += 1
    doublelst.append(count)

print(doublelst)
result = 0
for item in doublelst:
    result = result + item // 2

print(result)

count = 0
for item in setlst:
    count += lst.count(item) // 2

print(count)
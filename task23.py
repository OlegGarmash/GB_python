'''
Дан список, состоящий из целых чисел.
Напишите программу, которая подсчитает количество элементов списка,
больших предыдущего (элемента с предыдущим номером)
Input: [0, -1, 5, 2, 3]
Output: 2 (-1 < 5, 2 < 3)
'''

import random

lenlst = int(input("Введите длину списка: "))
count = 0
lst = []

for i in range(lenlst):
    lst.append(random.randint(1, 10))
    if lst[i] > lst[i-1]:
        count += 1

print(lst)
print(count)
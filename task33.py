'''
Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1
'''

import random

mark = [random.randint(1,5) for _ in range(10)]
print(mark)

minmark = 5
maxmark = 1
for i in mark:
    if maxmark < i:
        maxmark = i
    if minmark > i:
        minmark = i

for i in range(len(mark)):
    if mark[i] == maxmark:
        mark[i] = minmark

print(mark)
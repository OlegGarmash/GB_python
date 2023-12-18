'''
Дан массив, состоящий из целых чисел.
Напишите программу, которая в данном массиве определит количество элементов,
у которых два соседних и, при этом, оба соседних элемента меньше данного.
Сначала вводится число N — количество элементов в массиве
Далее записаны N чисел — элементы массива.
Массив состоит из целых чисел.
Ввод:
5
1 2 3 4 5
Вывод:
0
Ввод:
5
1 5 1 5 1
Вывод:
2
'''
import random

lenlst_n = int(input('Введите длину списка N: '))
lst_n = [random.randint(0, 10) for _ in range(lenlst_n)]

result = 0
print(lst_n)

for i in range(1, len(lst_n) - 1):
    if lst_n[i - 1] < lst_n[i] > lst_n[i + 1]:
        result += 1

#result = [i for i in range(1, lenlst_n - 1) if lst_n[i - 1] < lst_n[i] > lst_n[i + 1]]

print(result)
#print(len(result))

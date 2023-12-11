'''
Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах. Пользователь вводит 2 числа.
n - кол-во элементов первого множества.
m - кол-во элементов второго множества.
Затем пользователь вводит сами элементы множеств.
'''

import random

lenlst_1 = int(input("Введите длину списка: "))
lenlst_2 = int(input("Введите длину списка: "))
lst_1 = []
lst_2 = []

for _ in range(lenlst_1):
    lst_1.append(random.randint(-10, 10))

for _ in range(lenlst_2):
    lst_2.append(random.randint(-10, 10))

print(lst_1)
print(set(lst_1))
print(lst_2)
print(set(lst_2))

result = list(set(lst_1).intersection(set(lst_2)))
# result.sort() # сортировка
# print(result)
for i in range(len(result)):
    for n in range(len(result) - 1):
        if result[i] < result[n]:
            temp = result[i]
            result[i] = result[n]
            result[n] = temp

print(f'Общие значения: {result}')
print(*result, sep=' ')

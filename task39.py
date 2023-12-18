'''
Даны два массива чисел. Требуется вывести те элементы первого массива
(в том порядке, в каком они идут в первом массиве), которых нет во втором массиве.
Пользователь вводит  число N - количество элементов в первом массиве,
затем N чисел - элементы массива.
Затем число M - количество элементов во втором массиве.
Затем элементы второго массива
Ввод:
7
3 1 3 4 2 4 12
6
4 15 43 1 15 1
Вывод: 3 3 2 12
(каждое число вводится с новой строки)
'''
import random

lenlst_n = int(input('Введите длину списка N: '))
lst_n = [random.randint(0, 10) for _ in range(lenlst_n)]

# for _ in range(lenlst_n):
#     lst_n.append(int(input(f'Введите элемент № {i}: ')))

lenlst_m = int(input('Введите длину списка M: '))
lst_m = [random.randint(0, 10) for _ in range(lenlst_m)]

# for _ in range(lenlst_m):
#     lst_m.append(int(input(f'Введите элемент № {i}: ')))

diff = []
setlst_m = set(lst_m)
for item in lst_n:
    if item not in setlst_m:
        diff.append(item)

# data = [i for i in list1 if i not in list2]

print(lst_n)
print(lst_m)
print(diff)

change = set(lst_n).difference(lst_m)
print(change)
result = [i for i in lst_n if i in change]
print(result)
print(result := [i for i in lst_n if i in change])
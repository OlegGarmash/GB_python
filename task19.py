'''
Дана последовательность из N целых чисел и число K.
Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо,
K – положительное число.
Input:   [1, 2, 3, 4, 5] k = 3
Output:  [4, 5, 1, 2, 3]
'''

lst = [1, 2, 3, 4, 5]
lst2 = []
k = 3

# for i in lst:
#     lst2.append(lst[i-k])

for i in range(len(lst)):
    lst2.append(lst[(i + k) % len(lst)])
print(lst2)

# my_list = [1, 2, 3, 4, 5]
# k = 3
# shifted_list = my_list[k:] + my_list[:k]
#
# print(shifted_list)

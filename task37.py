'''
Дано натуральное число N и последовательность из N элементов.
Требуется вывести эту последовательность в обратном порядке.
Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
Input:    2 -> 3 4
Output: 4 3
'''

def reverse_lst(n):
    if n == 0:
        return
    x = int(input())
    reverse_lst(n - 1)
    print(x, end=' ')

num = int(input('Введите длину списка: '))
reverse_lst(num)

def rec_input(num: int):
    if num == 0:
        return ''
    s = input('Введите число: ')
    return rec_input(num - 1) + s + ' '

print(rec_input(5))
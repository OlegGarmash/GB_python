'''
 Требуется вывести все целые степени двойки (т.е. числа вида 2k),
 не превосходящие числа N.
 10 -> 1 2 4 8
'''

numberMax = int(input("Введите число N: "))
numberPow = 1
count = 1
while numberMax >= numberPow:
    print(numberPow)
    numberPow = 2 ** count
    count += 1


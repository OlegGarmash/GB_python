'''
Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n(само число)
Input: 5
Output: yes
'''

import random

x = int(input('Введите число: '))

answer = True
for i in range(3, int(x ** 0.5), 2):
    if x % i == 0:
        answer = False

print(answer)

def is_prime(number: int) -> bool:
    if number in range(3):
        return True
    if not number % 2:
        return False
    for i in range(3, int(number ** 0.5), 2):
        if not number % i:
            return False
    return True

print(is_prime(x))

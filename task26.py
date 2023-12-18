'''
Напишите программу, которая на вход принимает два числа A и B,
и возводит число А в целую степень B с помощью рекурсии.
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8
'''


def powerup(a, b):
    if b == 1:
        return a
    else:
        return a * powerup(a, b - 1)


# a = int(input('Введите число А: '))
# b = int(input('Введите степень B: '))

#print(powerup(a, b))
print(powerup(a = 2, b = 3))
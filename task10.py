'''
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть,
чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть.
5 -> 1 0 1 1 0
2
'''

import random

coins = int(input("Введите количество монет: "))

coinTials = 0
coinEagle = 0

for _ in range(coins):
    coinSide = random.randint(0, 1)
    print(coinSide, end=" ")
    if coinSide == 0:
        coinTials += 1
    else:
        coinEagle += 1

if coinTials < coinEagle:
    print(f'\nНужно перевернуть монет: {coinTials}')
else:
    print(f'\nНужно перевернуть монет: {coinEagle}')

'''
Для автотеста:
coinTials = 0
coinEagle = 0
for i in range(len(coins)):
    if coins[i] == 0:
        coinTials += 1
    else:
        coinEagle += 1

if coinTials < coinEagle:
    print(coinTials)
else:
    print(coinEagle)
'''
# За день машина проезжает n километров.
# Сколько дней нужно, чтобы проехать маршрут длиной m километров?
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
# Input: n = 700 m = 750
# Output: 2

n = int(input("Введите количество км в день "))
m = int(input("Введите количество км маршрута "))
result = (n+m-1)//n
print(result)

import math
print(f'Round {round(result)}')        #округление математически
print(f'Floor {math.floor(result)}')   #округление вниз
print(f'Ceil {math.ceil(m/n)}')       #округление вверх

#bool
days = m // n + bool(m % n != 0)
print(f'Bool {days}')
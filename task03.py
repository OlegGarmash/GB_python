# В некоторой школе решили набрать три новых математических класса и
# оборудовать кабинеты для них новыми партами.
# За каждой партой может сидеть два учащихся.
# Известно количество учащихся в каждом из трех классов.
# Выведите наименьшее число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

import math
class1 = int(input("First class: "))
class2 = int(input("Second class: "))
class3 = int(input("Third class: "))

result = (math.ceil(class1 / 2)) + ((class2 // 2) + class2 % 2) + ((class3 // 2) + class3 % 2)
print(f"Ceil: {result}")

total = (class1 + 1) // 2 + (class2 + 1) // 2 + (class3 + 1) // 2
print(total)
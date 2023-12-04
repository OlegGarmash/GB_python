'''
 Иван Васильевич пришел на рынок и решил купить два арбуза:
 один для себя, а другой для тещи.
 Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче.
 Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз?
 Помогите ему! Пользователь вводит одно число N – количество арбузов.
 Вторая строка содержит N чисел, записанных на новой строчке каждое.
 Здесь каждое число – это масса соответствующего арбуза
 Input: 5 -> 5 1 6 5 9
 Output: 1 9
'''

import random

arbuz = int(input("Введите количество арбузов: "))

MIN_WEIGHT = 1
MAX_WEIGHT = 30

# max_ = float('Inf')
# min_ = float('-Inf')

arbuzmax, arbuzmin = MIN_WEIGHT, MAX_WEIGHT

for _ in range(arbuz):
    arbuzweight = random.randint(MIN_WEIGHT, MAX_WEIGHT)
    print(arbuzweight, end=" ")
    if arbuzmax < arbuzweight:
        arbuzmax = arbuzweight
    if arbuzmin > arbuzweight:
        arbuzmin = arbuzweight

print(f"\nСамый лёгкий арбуз весит, кг: {arbuzmin}\nСамый тяжёлый арбуз весит, кг: {arbuzmax}")

'''
В фермерском хозяйстве в Карелии выращивают чернику.
Она растет на круглой грядке, причем кусты высажены только по окружности.
Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
собирает ягоды с этого куста и с двух соседних с ним. Напишите программу для нахождения максимального числа ягод,
которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
'''

import random

gardensize = int(input("Введите длину грядки: "))

gardenlst = []
gardentrio = []

for _ in range(gardensize):
    gardenlst.append(random.randint(1, 10))

for i in range(len(gardenlst)):
    if i == len(gardenlst) - 1:
        gardentrio.append(gardenlst[i - 1] + gardenlst[i] + gardenlst[0])
    else:
        gardentrio.append(gardenlst[i - 1] + gardenlst[i] + gardenlst[i + 1])

result = 0
for i in range(len(gardentrio)):
    if result < gardentrio[i]:
        result = gardentrio[i]

print(gardenlst)
print(gardentrio)
print(result)

# bushes = [random.randint(1,15) for _ in range(10)]
#
# print(bushes)
#
# max_berries = 0
# for i in range(len(bushes)):
#     total = bushes[i-2] + bushes[i-1] + bushes[i]
#     if total > max_berries:
#         max_berries = total
#
# print(max_berries)

# total = bushes[i-2] + bushes[i-1] + bushes[i]
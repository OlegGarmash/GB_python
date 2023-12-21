'''
Планеты вращаются вокруг звезд по эллиптическим орбитам.
Назовем самой далекой планетой ту, орбита которой имеет самую большую площадь.
Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит планет найдет ту,
по которой вращается самая далекая планета.
Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет,
зато искусственные спутники были были запущены на круговые орбиты.
Результатом функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты.
Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее эллипса.
Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины полуосей эллипса.
При решении задачи используйте списочные выражения.
Подсказка: проще всего будет найти эллипс в два шага: сначала вычислить самую большую площадь эллипса,
а затем найти и сам эллипс, имеющий такую  площадь.
Гарантируется, что самая далекая планета ровно одна
'''

# import math
#
#
# def s_of_irbits(a, b):
#     s = math.pi * a * b
#     return s
#
# def find_farthest_orbit(user_list):
#     user_max = 0
#     for i in range(len(user_list)):
#         if user_list[i] > user_max:
#             user_max = user_list[i]
#     return user_max
#
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# fixed_orbits = []
# for item in orbits:
#     if item[0] != item[1]:
#         fixed_orbits.append(item)
#
# s = list(map(lambda orbit: s_of_irbits(fixed_orbits[0], fixed_orbits[1]), fixed_orbits))
# print(s)

''' Алексей Логачев'''
# import math
#
# def s_of_orbits(a,b):
#     s = math.pi*a*b
#     return s
#
# def find_farthest_orbit(user_list):
#     user_max = 0
#     for i in range(len(user_list)):
#         if user_list[i] > user_max:
#             user_max = user_list[i]
#     return user_max
#
#
#
#
#
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# fixed_orbits = []
# for orbit in orbits:
#     if orbit[0] != orbit[1]:
#         fixed_orbits.append(orbit)
# print(fixed_orbits)
# s = list(map(lambda orbit: s_of_orbits(orbit[0], orbit[1]), fixed_orbits))
# print(s)

''' Акмаль'''
# def find_farthest_orbit(orbits):
#     square_orbits = [(i[0] != i[1]) * i[0] * i[1] for i in orbits]
#     return orbits[square_orbits.index(max(square_orbits))]
#
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))

''' Преподователь '''
from random import randint

print(planets := [(randint(1, 15), randint(1, 15)) for _ in range(10)])
print(planets := set(filter(lambda x: x[0] != x[1], planets)))
print(sorted(planets, key = lambda x: x[0] * x[1], reverse=True))

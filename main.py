# print("hello")
#
# list_1 = [12, 7, -1, 21, 0]
# for i in range(len(list_1)):
#     print(i)

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = []
#
# for item in data:
#     if item % 2 == 0:
#         res.append((item, item ** 2))
#
# print(res)

# def select(f, col):
#     return [f(x) for x in col]
#
# def where (f, col):
#     return [x for x in col if f(x)]
#
# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int, data)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(select(lambda x: (x, x**2), res))
# print(res)

# list_1 = [x for x in range(1, 20)]
# print(list_1)
#
# list_1 = list(map(lambda x: x + 10, list_1))
# print(list_1)

# data = '15 220 36 15 89 4 2 365 120 55'
# print(data)
#
# # data = data.split()
# # print(data)
#
# data = list(map(int, data.split()))
# print(data)

''''''
# data = [15, 220, 36, 15, 89, 4, 2, 365, 120, 55]
# res = list(filter(lambda x: x % 10 == 5, data))
# print(res)

''''''
# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = map(int, data)
#
# res = filter(lambda x: x % 2 == 0, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)

''' map '''
# a = '123456789'
# print(list(a))
# a = list(a)
#
# # for i in range(len(a)):
# #     a[i] = int(a[i])
# #
# # print(a)
#
# a = list(map (int, a))
# print(a)

''' lambda '''
# a = '123456789'
# a = list(a)
# print(a)
#
# a = [int(x) for x in a if int(x) % 2 == 0]
# print(a)
#
# #a = list(map (int, a))
# #b = []
# # for item in a:
# #     if item % 2 ==0:
# #         b.append(item)
#
# b = list(map(int, filter(lambda x: int(x) % 2 == 0, a)))
# print(b)
#
# # a = list(map (lambda x: x * 2, a))
# # print(a)

''' enumerate '''
# a = 'asdfghjklertyui'
# a = list(a)
#
# for i, item in enumerate(a, 1):
#     print(i, item)
#
''' zip '''
# a = 'asdfghjklertyui'
# b = '123456789'
# a = list(a)
# # c = []
# # c = list(zip(a, b))
# # # for i in range(len(b)):
# # #     c.append((a[i], b[i]))
# # print(c)
# from itertools import zip_longest
# c = list(zip_longest(a, b))
# print(c)
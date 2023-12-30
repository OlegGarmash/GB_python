with open('task53_main.txt') as file:
    data = {}
    for line in file:
        key, *value = line.split()
        data[key] = value

print(data)

with open('task53_homework.txt', 'w') as file:
    for key, value in data.items():
        file.write(f'{key} {value[0]} {value[1]} {value[2]}\n')


# def close_file():
#     return 0


# fruit = {0: [1, 1], 1: [2, 2], 2: [3, 3]}
# # print(len(fruit))
# fruit[len(fruit)] = [4, 'qwe']
# # print(len(fruit))
# # print(fruit)
# fruit[len(fruit)] = ['asd', 5]
# # print(len(fruit))
# # print(fruit)
# fruit[len(fruit) + 1] = ['qwe', 'aSD']
# # print(len(fruit))
# # print(fruit)
# data = fruit[1]
# # print(data)
# data[1] = 'asd'
# fruit[1] = data
# # print(len(fruit))
# # print(fruit)
# fruit[0][0] = 'Asd'
# print(fruit)
# fruit[len(fruit) + 2] = ['qwe', 'aSD']
# fruit[len(fruit) + 2] = ['qwe', 'aSD']
#
# # data = input('¬ведите данные дл€ поиск:\n')
# # for key, value in fruit.items():
# #     print(f'id {key}:', end='\t')
# #     print(*list(fruit[key]), sep=', ')
# temp = 3
# del fruit[temp]
# print(fruit)
# # for key in fruit:
# #     if key > temp:
# #         fruit[key] = fruit[key-1]
# #
# # print(fruit)
#
# lst = list(fruit.keys())
# print(lst)
# tmp = list()
# for i in range(len(lst)):
#     if (lst[i] - lst[i - 1]) > 1:
#         tmp.append(lst[i] - 1)
#
# print(tmp)
# # print(temp)
#
# print(list(fruit.keys())[len(fruit) - 1] + 1)
# print(list(fruit.keys())[len(fruit) - 1] + 1)
#
# # f = open('text.txt', 'r')
# # for line in f:
# #     print(line)
# # f.writelines(str(fruit))
# # f.close()

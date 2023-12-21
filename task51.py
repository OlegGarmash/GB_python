'''
Напишите функцию same_by(characteristic, objects), которая проверяет,
все ли объекты имеют одинаковое значение некоторой характеристики, и возвращают True, если это так.
Если значение характеристики для разных объектов отличается - то False.
Для пустого набора объектов, функция должна возвращать True.
Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.
'''


# def same_by(characteristic, objects):
#     if len(objects) == 0:
#         return True
#     first_object = characteristic(objects[0])
#     for i in range(len(objects)):
#         if first_object != characteristic(objects[i]):
#             return True
#
#
# values = [0, 2, 10, 6]
# if same_by(lambda x: x % 2, values):
#     print("same")
# else:
#     print("different")

''' Преподаватель '''
def same_by(characteristic, values):
    return len(set(map(characteristic, values))) < 2

a = list('123456789')
print(same_by(lambda x: x.isdigit(), a))

values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print("same")
else:
    print("different")

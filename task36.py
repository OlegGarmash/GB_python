'''
Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.
print_operation_table(lambda x, y: x * y)
'''


def print_operation_table(operation, num_rows=9, num_columns=9):
    if num_rows > 1 and num_columns > 1:
        for i in range(num_columns):
            if i < num_columns - 1:
                print(i + 1, end=' ')
            else:
                print(i + 1, end='\n')
        for i in range(1, num_columns):
            print(i + 1, end=' ')
            for j in range(1, num_rows):
                if j < num_rows - 1:
                    print(operation(i + 1, j + 1), end=' ')
                else:
                    print(operation(i + 1, j + 1), end='\n')
    else:
        print('ОШИБКА! Размерности таблицы должны быть больше 2!')


print_operation_table(lambda x, y: x * y, 3, 3)
print()
print_operation_table(lambda x, y: x + y, 4, 4)
print()
print_operation_table(lambda x, y: x - y, 5, 5)
print()
print_operation_table(lambda x, y: x / y, 4, 4)
print()
print_operation_table(lambda x, y: x * y)
print()
print_operation_table(lambda x, y: x * y, 1, 2)

'''
Дано натуральное число A > 1.
Определите, каким по счету числом Фибоначчи оно является,
то есть выведите такое число n, что φ(n)=A.
Если А не является числом Фибоначчи, выведите число -1.
Input:     5
Output:  6
'''


'''
a = int(input("Введите число А: "))
count = 2
temp1 = 1
temp2 = 0
result = 0

while a > result:
    count += 1
    result = temp1 + temp2
    temp2 = temp1
    temp1 = result

if a == 0:
    print(f"Позиция 1")
elif a == 1:
    print(f"Позиция 2")
elif a == result:
    print(f"Позиция {count}")
else:
    print("-1")
'''

number = int(input("Введите число А: "))

count = 2
temp1, temp2 = 0, 1

while temp1 + temp2 < number:
    count += 1
    temp1, temp2 = temp2, temp1 + temp2

if number == 0:
    print(f"Позиция 1")
elif number == 1:
    print(f"Позиция 2 или 3")
elif number == temp1 + temp2:
    print(f"Позиция {count}")
else:
    print("-1")
'''
 Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и
 получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером,
 где сумма первых трех цифр равна сумме последних трех.
 Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
 Вам требуется написать программу, которая проверяет счастливость билета.
 385916 -> yes
 123456 -> no
'''

bilet = int(input("Введите номер билета: "))

bilet1 = bilet % 1000
bilet2 = bilet // 1000

bilet1Sum = 0
bilet2Sum = 0

while bilet1 > 0:
    x = bilet1 % 10
    bilet1Sum = bilet1Sum + x
    bilet1 = bilet1 // 10

while bilet2 > 0:
    x = bilet2 % 10
    bilet2Sum = bilet2Sum + x
    bilet2 = bilet2 // 10

if bilet1Sum == bilet2Sum:
    print("Yes")
else:
    print("No")
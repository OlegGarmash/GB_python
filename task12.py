'''
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
а Катя должна их отгадать. Для этого Петя делает две подсказки.
Он называет сумму этих чисел S и их произведение P.
Помогите Кате отгадать задуманные Петей числа.
4 4 -> 2 2
5 6 -> 2 3
'''

sumXY = int(input("Введите сумму чисел X и Y: "))
multiXY = int(input("Введите произведение чисел X и Y: "))

numberX = 1

for i in range(1, 1001):
    numberY = 1
    for j in range(1, 1001):
        while numberX >= numberY:
            if numberX + numberY == sumXY and numberY * numberX == multiXY:
                print(f'{numberY} {numberX}', end=' ')
            numberY += 1
    numberX += 1

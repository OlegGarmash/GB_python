'''
В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
В случае с английским алфавитом очки распределяются так:
● A, E, I, O, U, L, N, S, T, R – 1 очко;
● D, G – 2 очка;
● B, C, M, P – 3 очка;
● F, H, V, W, Y – 4 очка;
● K – 5 очков;
● J, X – 8 очков;
● Q, Z – 10 очков.
А русские буквы оцениваются так:
● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
● Д, К, Л, М, П, У – 2 очка;
● Б, Г, Ё, Ь, Я – 3 очка;
● Й, Ы – 4 очка;
● Ж, З, Х, Ц, Ч – 5 очков;
● Ш, Э, Ю – 8 очков;
● Ф, Щ, Ъ – 10 очков.
Напишите программу, которая вычисляет стоимость введенного пользователем слова.
Будем считать, что на вход подается только одно слово,
которое содержит либо только английские, либо только русские буквы.
Ввод: ноутбук
Вывод: 12
'''

one = {'A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'}
two = {'D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У'}
three = {'B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я'}
four = {'F', 'H', 'V', 'W', 'Y', 'Й', 'Ы'}
five = {'K', 'Ж', 'З', 'Х', 'Ц', 'Ч'}
eight = {'J', 'X', 'Ш', 'Э', 'Ю'}
ten = {'Q', 'Z', 'Ф', 'Щ', 'Ъ'}

result = 0

word = input('Введите слово: ')
for letter in word:
    if letter.upper() in one:
        result += 1
    elif letter.upper() in two:
        result += 2
    elif letter.upper() in three:
        result += 3
    elif letter.upper() in four:
        result += 4
    elif letter.upper() in five:
        result += 5
    elif letter.upper() in eight:
        result += 8
    elif letter.upper() in ten:
        result += 10

print(f'Сумма букв равна: {result}')

# scrabble = {1: 'AEIOULNSTRАВЕИНОРСТ', 2: 'DGДКЛМПУ', 3: 'BCMPБГЁЬЯ', 4: 'FHVWYЙЫ', 5: 'KЖЗХЦЧ', 8: 'JXШЭЮ', 10: 'QZФЩЪ'}
# word = input('Введите слово: ')
# word = word.upper()
# score = 0
# for letter in word:
#     for points, letters in scrabble.items():
#         if letter in letters:
#             score += points
#
# print(score)

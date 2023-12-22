'''
Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
Вам стоит написать программу. Винни-Пух считает, что ритм есть,
если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
Ввод: пара-ра-рам рам-пам-папам па-ра-па-дам
Вывод: Парам пам-пам
'''

stroka = 'пара-ра-рам'
stroka = stroka.split()

symbols = {'у', 'е', 'ы', 'а', 'о', 'э', 'я', 'и', 'ю'}
lst = []
for item in stroka:
    count = 0
    for i in item:
        if i in symbols:
            count += 1
    lst.append(count)


def func(lst):
    count = 0
    for i in range(len(lst) - 1):
        if lst[i] == lst[i + 1]:
            count += 1
        else:
            count += -1
    if count == len(lst) - 1:
        return True
    else:
        return False


print(stroka)
print(count)
print(lst)
print(len(lst))

if len(lst) > 1:
    if func(lst) == True:
        print('Парам пам-пам')
    else:
        print('Пам парам')
else:
    print('Количество фраз должно быть больше одной!')
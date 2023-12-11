'''
Пользователь вводит текст(строка).
Словом считается последовательность непробельных символов идущих подряд,
слова разделены одним или большим числом пробелов.
Определите, сколько различных слов содержится в этом тексте.
Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
Output: 13
'''

words = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
text = words.lower().replace('.', ' ').split()
setwords = set(text)

# count = 0
# for i in setwords:
#     count += 1

print(f'Различных слов: {len(setwords)}')
print(setwords)
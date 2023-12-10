'''
Напишите программу для печати всех уникальных значений в словаре.
Input:  [{"V":"S001"}, {"V":"S002"}, {"VI":"S001"}, {"VI":"S005"}, {"VII":"S005"}, {"V":"S009"}, {"VIII":"S007"}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
'''

data = [{"V":"S001"}, {"V":"S002"}, {"VI":"S001"}, {"VI":"S005"}, {"VII":"S005"}, {"V":"S009"}, {"VIII":"S007"}]

keys = set()
values = set()

for dct in data:
    for key, value in dct.items():
        keys.add(key)
        values.add(value)

print(keys)
print(values)

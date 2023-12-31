# Вагоны в электричке пронумерованы натуральными числами,
# начиная с 1 (при этом иногда вагоны нумеруются от «головы» поезда,
# а иногда – с «хвоста»; это зависит от того, в какую сторону едет электричка).
# В каждом вагоне написан его номер. Витя сел в i-й вагон от головы поезда и обнаружил,
# что его вагон имеет номер j. Он хочет определить, сколько всего вагонов в электричке.
# Напишите программу, которая будет это делать или сообщать,
# что без дополнительной информации это сделать невозможно.
# Input: 3 4(ввод на разных строках)
# Output: 6

real_number = int(input("The real number: "))
our_number = int(input("Our number: "))

if real_number == our_number:
    result = "Not enough info"
else:
    result = f"Всего {real_number + our_number - 1} вагонов"

print(result)
# создаю словарь с нулевыми значениями
counts = {}
for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    counts[i] = 0

# открываю файл целиком, перевожу в верхний регистр
with open("The Red Room-1.txt", "r", encoding='utf-8', errors='replace') as file:
    read_lines = file.read().strip().upper()

# определяем количество слов в книге
words = read_lines.split()
word_count = len(words)

# первый цикл перебирает файл, второй цикл преребирает словарь
for j in words:
    for k, v in counts.items():
        if k in j:
            counts[k] += 1

# вывожу результат для всех 26 букв
for k, v in counts.items():
    print(f"Буква '{k}' встречается в {round((v / word_count) * 100, 2)} % слов.")

# нахожу самую редкую букву
smallest_count = min(counts.values())

for k, v in counts.items():
    if v == smallest_count:
        print(f"Самая редкая буква в книге: {k}")
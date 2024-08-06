counts = {}
for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    counts[ch] = 0
print(counts)
counts_1 = dict(counts)

# открываю файл целиком, перевожу в верхний регистр
with open("The Red Room-1.txt", "r", encoding='utf-8', errors='replace') as file:
    read_lines = file.read().strip()
    read_lines = read_lines.upper()

# первый цикл перебирает файл, второй цикл преребирает словарь
for i in read_lines:
    for k, v in counts.items():
        if i == k:
            counts[i] += 1 # обновляем счетчик

# вывожу результат для всех 26 букв
for k, v in counts.items():
    print(f"Буква {k} встречается: {v} раз.")

# нахожу самую редкую букву
smallest_count = min(counts.values())

for k, v in counts.items():
    if v == smallest_count:
        print(f"Самая редкая буква в книге: {k}")

# в каком % слов встречается каждая буква
with open("The Red Room-1.txt", "r", encoding='utf-8', errors='replace') as file:
    content = file.read()
    words = content.split()
    print(words)
    word_count = len(words)

print(f'Количество слов в книге: {word_count} шт.')

for j in words:
    for key, value in counts_1.items():
        if key in j:
            counts_1[key] += 1


print(counts_1)
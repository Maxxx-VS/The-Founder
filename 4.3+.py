# def sum_to(n):
#     if n <= 0 :
#         return 0 # Базовый случай
#     else:
#         return n + sum_to(n-1) # Рекурсивный случай
#     # Вычисляем сумму всех целых чисел от нуля до заданного n
#
# n = int(input("Введите положительное целое число: "))
# total = sum_to(n)
# print("Сумма целых чисел от нуля до", n, "равна", total)


# def sum_to():
#     n = input("Введите число для сложения (пустая строка - остановить ввод): ")
#     if n <= '':
#         return 0
#     else:
#         return int(n) + sum_to()
#
# total = sum_to()
# print(f"Сумма чисел равна {total}")

# def evklid(a, b):
#     if b == 0:
#         return a
#     else:
#         return evklid(b, a % b)
#
# a = int(input("Введите первое положительное число: "))
# b = int(input("Введите второе положительное число: "))
# div = evklid(a, b)
# print(f'Наибольший общий делитель чисел {a} и {b} = {div}')

word_dict = {
    "A": "Alpha", "J": "Juliet", "S ": "Sierra", "B": "Bravo", "K": "Kilo", "T": "Tango", "C": "Charlie",
    "L": "Lima", "U": "Uniform", "D": "Delta", "M": "Mike", "V": "Victor", "E": "Echo", "N": "November",
    "W": "Whiskey", "F": "Foxtrot", "O": "Oscar", "X": "Xray", "G": "Golf", "P": "Papa", "Y": "Yankee",
    "H": "Hotel", "Q": "Quebec", "Z": "Zulu", "I": "India", "R": "Romeo"}

def abs_dict(word):

    if not word:
        return None
    first_letter = word[0]
    rest_of_word = word[1:]
    abs_dict = word_dict.get(first_letter, '')



word = input("Введите слово: ")
total = alfa(word)
print(total)


alphabet = {
'a': 'Alpha', 'b': 'Bravo', 'c': 'Charlie', 'd': 'Delta', 'e': 'Echo', 'f': 'Foxtrot',
'g': 'Golf', 'h': 'Hotel', 'i': 'India', 'j': 'Juliett', 'k': 'Kilo', 'l': 'Lima',
'm': 'Mike', 'n': 'November', 'o': 'Oscar', 'p': 'Papa', 'q': 'Quebec', 'r': 'Romeo',
's': 'Sierra', 't': 'Tango', 'u': 'Uniform', 'v': 'Victor', 'w': 'Whiskey',
'x': 'Xray', 'y': 'Yankee', 'z': 'Zulu'
}

def encode_word(word):
    word = ''.join(filter(str.isalpha, word.lower()))

    if not word:
        return ''

# Рекурсивный случай - обрабатываем первую букву слова и рекурсивно вызываем функцию для оставшейся части слова
    first_letter = word[0]
    rest_of_word = word[1:]
    encoded_word = alphabet.get(first_letter, '') # Получаем соответствующее слово для буквы
    if encoded_word:
    # Если для буквы есть соответствующее слово, добавляем его к результату и вызываем функцию рекурсивно для оставшейся части слова
        return encoded_word + ' ' + encode_word(rest_of_word)
    else:
    # Если для буквы нет соответствующего слова, пропускаем ее и вызываем функцию рекурсивно для оставшейся части слова
        return encode_word(rest_of_word)

# Пример использования функции
word = input("Введите слово: ")
encoded_word = encode_word(word)
print(encoded_word)
















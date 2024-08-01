# word = input("Введите слова (пустая строка - для окончания ввода): ")
# array_word = []
#
# while word != "":
#     if word not in array_word:
#         array_word.append(word)
#         word = input("Введите слова (пустая строка - для окончания ввода): ")
#     else:
#         word = input("Введите слова (пустая строка - для окончания ввода): ")
#
# print(*array_word, sep='\n')

# nums = 100
#
# for i in range(1, nums+1):
#     if i % 3 == 0 and i % 5 == 0:
#         print(f'Число {i}: Fizz-Buzz')
#     elif i % 3 == 0:
#         print(f'Число {i}: Fizz')
#     elif i % 5 == 0:
#         print(f'Число {i}: Buzz')

# nums = input("Введите очередное число (пустая строка - для окончания ввода): ")
#
# array_nums, array_nums_less, array_nums_equals, array_nums_more = [], [], [], []
#
# while nums != "":
#         array_nums.append(int(nums))
#         nums = input("Введите очередное число (пустая строка - для окончания ввода): ")
#
# average_nums = sum(array_nums) / len(array_nums)
#
# for i in array_nums:
#     if i < average_nums:
#         array_nums_less.append(i)
#     elif i > average_nums:
#         array_nums_more.append(i)
#     else:
#         array_nums_equals.append(i)
#
# print(f'Среднее значение ряда чисел: {average_nums}')
# print(f'Числа ниже среднего: {array_nums_less}')
# print(f'Числа равные среднему: {array_nums_equals}')
# print(f'Числа выше среднего: {array_nums_more}')

# numbers = int(input("Введите предельное число: "))
# simple_numbers = []
#
# for i in range(numbers+1):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#         else:
#             simple_numbers.append(i)
#             break
#
# print(simple_numbers)

# word = input("Введте слово: ")
# total = 0
# word_dict = {
#     'A':1, 'E':1, 'I':1, 'L':1, 'N':1, 'O':1, 'R':1, 'S':1, 'T':1,  'U':1,
#     'D':2, 'G':2,
#     'B':3, 'C':3, 'M':3, 'P':3,
#     'F':4, 'H':4, 'V':4, 'W':4, 'Y':4,
#     'K':5,
#     'J':8, 'X':8,
#     'Q':10, 'Z':10}
#
# for i in word:
#     for key, value in word_dict.items():
#         if i.upper() == key:
#             total += value
#
# print(total)







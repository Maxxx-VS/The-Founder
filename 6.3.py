# создаю словарь англ. языка со значениями = 0
counts = {}
for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ": # {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
    counts[ch] = 0

# открываю файл целиком, перевожу в верхний регистр
with open("The Red Room-1.txt", "r") as file:
    read_lines = file.read()
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


# from bs4 import BeautifulSoup
# import requests
#
# title_news = []
#
# url = ("https://2051.vision/category/ii/") # Зададим адрес новостного сайта для GET-запроса библиотеки requests
# html = requests.get(url).text # Извлекаем из тела ответа текстовые данные
# soup = BeautifulSoup(html, 'html5lib') # Применяем к данным анализатор html5lib
#
#
# for link in soup.find_all('a', class_='td-image-wrap'):
#     title_news.append(link.get('title'))
#
# for i, news in enumerate(title_news):
#     print(i+1, news)




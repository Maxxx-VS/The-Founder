# import praw
#
# reddit = praw.Reddit(
#     client_id="SnZtTpUrZWaDRA5Df1b9fA",
#     client_secret="QUVOWDooW5Xyu26TdpbvfCchuPGY3g",
#     redirect_uri="http://localhost:8080",
#     user_agent="Old-Candidate-5364")
#
# top_posts = reddit.subreddit("all").top(limit=10)
#
# for post in top_posts:
#     print(post.title)
#
# post = next(reddit.subreddit("all").top(limit=1))
# top_comments = post.comments.list()[:5]
#
# for comment in top_comments:
#     print(comment.body)

# import requests
#
# BBC_API = 'ea502e6467cd4caaa4183fee68bc5c98'
# URL = f'https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={BBC_API}&pageSize=10'
# response = requests.get(URL)
#
# print(response)
# news_list = response.json()['articles']
#
# for i, news in enumerate(news_list):
#     print(f'{i+1} --> {news["title"]}')


# import requests
#
#
# URL = 'https://newsdata.io/api/1/latest?country=en&category=top&apikey=pub_500759ff2677aee76fd3438ec5e85eb1794f0'
# response = requests.get(URL)
#
# print(response)
#
# news_list = response.json()
# print(news_list)
#
# # for i, news in enumerate(news_list):
# #     print(f'{i+1} --> {news["title"]}')

# from bs4 import BeautifulSoup
# import requests
#
# title_news = []
#
# url = ("https://www.allyoucanread.com/spanish-newspapers/")
# html = requests.get(url).text
# soup = BeautifulSoup(html, 'html5lib')
#
# for link in soup.find_all('img', class_='link-arrow-img'):
#     print(link.get('title'))

import requests
import json

# SPAIN_API = 'pub_500759ff2677aee76fd3438ec5e85eb1794f0'
# URL = f'https://newsdata.io/api/1/latest?apikey={SPAIN_API}'
#
# response = requests.get(URL)
# print(response)
#
# news_list = response.json()
# titles = news_list['results']['title']
#
# print(news_list)
# print(titles)

# OpenWeatherMap
import requests
import json

API = '88e1d9b53f2f324d6004ee7e57cf40cc'
my_city = "omsk"
weather_city = my_city.strip().lower()
res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={my_city}&appid={API}&units=metric').json()
print(res)
print(f"Текущая погода в вашем городе: {res['main']['temp']} градусов Цельсия")
print(f"Скорость ветра: {res['wind']['speed']} м/сек")


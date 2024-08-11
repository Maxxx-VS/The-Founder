import os
import warnings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

FILE_PATH = 'the_movies_dataset'
dir_list = os.listdir(FILE_PATH)
warnings.filterwarnings('ignore')

# датафрейм из файла метаданных фильмов:
df = pd.read_csv('the_movies_dataset/movies_metadata.csv')

# очищаю данные
all_colums = df.columns
for i in all_colums:
    if i != 'release_date':
        df = df.drop([i], axis=1)
    else:
        df = df.rename(columns={'release_date': 'day_of_week'})

# получаю день недели из даты
day_of_week = pd.to_datetime(df['day_of_week'],
                             errors="coerce").apply(lambda x: x.strftime('%A') if not pd.isnull(x) else np.nan).value_counts()

day_of_week.plot(kind='bar',
                 title="Выпуск фильмов по дням недели",
                 xlabel="Дни недели",
                 ylabel="Количество релизов",
                 color='grey',
                 figsize=(5, 10))
plt.show()
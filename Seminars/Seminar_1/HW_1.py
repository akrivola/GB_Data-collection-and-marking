'''
ДОМАШНЕЕ ЗАДАНИЕ

Криволапов Антон

Задание с семинара
Сбор и разметка данных (семинары)
Урок 1. Основы клиент-серверного взаимодействия. Парсинг API
Ознакомиться с некоторые интересными API. https://docs.ozon.ru/api/seller/ https://developers.google.com/youtube/v3/getting-started https://spoonacular.com/food-api
Потренируйтесь делать запросы к API. Выберите публичный API, который вас интересует, и потренируйтесь делать API-запросы с помощью Postman. Поэкспериментируйте с различными типами запросов и попробуйте получить различные типы данных.
Сценарий Foursquare
Напишите сценарий на языке Python, который предложит пользователю ввести интересующую его категорию (например, кофейни, музеи, парки и т.д.).
Используйте API Foursquare для поиска заведений в указанной категории.
Получите название заведения, его адрес и рейтинг для каждого из них.
Скрипт должен вывести название и адрес и рейтинг каждого заведения в консоль.

Вместо сценария Foursquare я выберу более интересный для меня в настоящие момент сценарий
получения данных о криптовалюте с биржи Bybit, так как я изучаю API Bybit для написания торгового бота
'''

# Используем библиотеку Python для Bybit - pybit
# pip install pybit
# pip install pycryptodome

# Запрашиваем у пользователя интересующую его криптовалютную пару
symbol = input("Введите интересующую вас пару (например, BTCUSDT и т.д.) По умолчанию будут выводиться данные для BTCUSDT: ")

# Проверяем, ввел ли пользователь что-то или оставил поле пустым
if symbol == '':
    symbol = 'BTCUSDT'

# Выводим сообщение с выбранной категорией
print(f"Вы выбрали категорию: {symbol}")

import pprint
import datetime as dt
import json
from pybit.unified_trading import HTTP
import pandas as pd

interval = 60
start = str(int(dt.datetime(2024,1,1).timestamp()*1000))
end = str(int(dt.datetime(2024,5,9).timestamp()*1000))

print(f"Исторические данные по {symbol} на споте за период с {start} по {end}:")

session = HTTP(testnet=True)
response=session.get_kline(
    category="spot",
    symbol=symbol,
    interval=interval,
    start=start,
    end=end,
)

# Выводим данные за заданный период времени

data = response["result"]["list"]
columns = ["t", "open", "high", "low", "close", "volume", "quoteVolume"]

df = pd.DataFrame(data, columns=columns)
df['t'] = pd.to_datetime(df['t'],unit='ms')

print(df)

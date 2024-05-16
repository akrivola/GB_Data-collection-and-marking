'''
1) Установите MongoDB на локальной машине, а также зарегистрируйтесь в онлайн-сервисе. https://www.mongodb.com/ https://www.mongodb.com/products/compass
2) Загрузите данные который вы получили на предыдущем уроке путем скрейпинга сайта с помощью Buautiful Soup в MongoDB и создайте базу данных и коллекции для их хранения.
3) Поэкспериментируйте с различными методами запросов.
'''

import json
from pymongo import MongoClient
import os
from pprint import pprint



# Подключение к MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client["mydatabase"]
collection = db["mycollection"]

# Очистка коллекции
collection.delete_many({})

# Определение пути к файлу JSON
json_file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'Seminar_2\\books_toscrape_data.json')

# Загрузка данных из файла JSON
with open(json_file_path) as file:
    data = json.load(file)

# Выгрузка данных в MongoDB
collection.insert_many(data)

# 1. Запрос для извлечения всех товаров из коллекции:

# result = collection.find({})
# for document in result:
#     pprint(document)

# 3. Запрос для извлечения товаров с количеством больше 10 единиц в наличии:

result = collection.find({"quantity": {"$gt": 20}})
for document in result:
    print(document)

client.close()
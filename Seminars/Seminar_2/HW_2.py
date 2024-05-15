'''
Урок 2. Парсинг HTML. BeautifulSoup
Выполнить скрейпинг данных в веб-сайта http://books.toscrape.com/ и извлечь информацию о всех книгах на сайте во всех
категориях: название, цену, количество товара в наличии (In stock (19 available)) в формате integer, описание.

Программа записывает результат в books_toscrape.log
Данные - в books_toscrape_data.json
'''

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from pprint import pprint
import re
import json
import logging

logging.basicConfig(filename='books_toscrape.log', level=logging.INFO)

# https://books.toscrape.com/catalogue/page-1.html
url = "https://books.toscrape.com/catalogue/"
direct_url = "https://books.toscrape.com/catalogue/page-"

headers = {
    "User-Agent": 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36'}

session = requests.session()

all_books = []
page = 1

while True:
    response = session.get(direct_url + str(page) + '.html', headers=headers)
    if response.status_code == 404:
        break
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all('li', {'class': 'col-xs-6 col-sm-4 col-md-3 col-lg-3'})

    for book in books:
        book_info = {}

        container = book.find('div', {'class': 'image_container'})

        link = url + container.find('a').get('href')

        title = container.find('img').get('alt')
        book_info['title'] = title

        price = book.find('p', {'class': 'price_color'}).getText()[1:]
        book_info['price'] = price

        response_inner = session.get(link, headers=headers)
        soup_inner = BeautifulSoup(response_inner.text, "html.parser")

        stock = soup_inner.find('p', {'class': 'instock availability'}).getText()
        result = re.search(r'\d+', stock)
        if result:
            quantity = int(result.group())
        else:
            quantity = 0

        book_info['quantity'] = quantity
        try:
            description = soup_inner.find('article', {'class': 'product_page'}).find('p', {'class': ''}).getText()
        except:
            print(f'No description for book {title}')
            logging.info(f'No description for book {title}')
            description = ''

        book_info['description'] = description

        all_books.append(book_info)
    print(f'Page {page} parced successfully')
    logging.info(f'Page {page} parced successfully')

    page += 1

with open('books_toscrape_data.json', 'w') as f:
    json.dump(all_books, f)

import pandas as pd

df = pd.DataFrame(all_books)
print(df)

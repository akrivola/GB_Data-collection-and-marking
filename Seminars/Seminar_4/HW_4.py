'''
Урок 4. Парсинг HTML. XPath
Выберите веб-сайт с табличными данными, который вас интересует.
Напишите код Python, использующий библиотеку requests для отправки HTTP GET-запроса на сайт и получения HTML-содержимого страницы.
Выполните парсинг содержимого HTML с помощью библиотеки lxml, чтобы извлечь данные из таблицы.
Сохраните извлеченные данные в CSV-файл с помощью модуля csv.

Ваш код должен включать следующее:

Строку агента пользователя в заголовке HTTP-запроса, чтобы имитировать веб-браузер и избежать блокировки сервером.
Выражения XPath для выбора элементов данных таблицы и извлечения их содержимого.
Обработка ошибок для случаев, когда данные не имеют ожидаемого формата.
Комментарии для объяснения цели и логики кода.

Примечание: Пожалуйста, не забывайте соблюдать этические и юридические нормы при веб-скреппинге.
'''

# Времени было мало, поэтому я взял не news.mail.ru, а сайт компании, в которой я работаю и собрал данные по автобакам
# c одной страницы
# сайт avto-baki.ru
# делал его наш веб-программист, код я его вижу в первый раз

from lxml import html
import requests
from pprint import pprint
import csv

header = {
    "User-Agent": 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36'}

url = 'https://avto-baki.ru/the-fuel/'
response = requests.get(url, headers=header)  # Делаем HTTP GET-запрос на сайт и получаем HTML-содержимое страницы
dom = html.fromstring(response.text)

items_list = []
items = dom.xpath("//div[@class='ms2_product']")  # Берем табличный элемент, содержащий информацию по одному объекту
# В цикле собираем данные по одному объекту
for item in items:
    item_info = {}

    try:
        name = item.xpath(".//a[@itemprop='name']/text()")[0]
        price = item.xpath(".//meta[@itemprop='price']/@content")[0]
        availability = item.xpath(".//span[@class='available']/text()")[0]

        item_info['Наименование'] = name
        item_info['Цена'] = int(price)
        item_info['Наличие'] = availability

        params = item.xpath(".//ul//li")
        for param in params:
            param_name = param.xpath("./text()")[0].strip()  # Удаляем лишние пробелы
            param_value = param.xpath("./span/text()")[0].strip()  # Удаляем лишние пробелы
            item_info[param_name] = param_value

        items_list.append(item_info)
    # При возникновении ошибки при получении данных из элемента, выводится сообщение об ошибке и обработка продолжается
    # для следующих элементов.
    except Exception as e:
        print(f"Ошибка при обработке элемента: {e}")

pprint(items_list)

# Вывод результатов в CSV файл
csv_file = open('result.csv', 'w', newline='')
csv_writer = csv.DictWriter(csv_file, fieldnames=items_list[0].keys())
csv_writer.writeheader()
csv_writer.writerows(items_list)
csv_file.close()

# функция, которая убирает лишние пробелы и :
def remove_extra_spaces_and_colon(input_string):
    result_string = " ".join(input_string.split())  # Убираем лишние пробелы
    result_string = result_string.replace(":", "")  # Убираем ":"
    return result_string

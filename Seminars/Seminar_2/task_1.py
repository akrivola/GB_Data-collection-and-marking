import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
# ua = UserAgent()

# url = "https://www.boxofficemojo.com/intl/?ref_=bo_nb_hm_tab"
url = "https://www.boxofficemojo.com"

headers = {"User-Agent": 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36'}
params = {"ref_": "bo_nb_hm_tab"}

session = requests.session()

response = session.get(url+"/intl", params=params, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
rows = soup.find_all('tr')

films = []

for row in rows[2:]:
    film = {}
    area_info = row.find('td',{'class': 'mojo-field-type-area_id'}).find('a')
    film['area'] = [area_info.getText(), url + area_info.get('href')]
    print()
# test_link = soup.find("a", {'class':'a-link-normal'})

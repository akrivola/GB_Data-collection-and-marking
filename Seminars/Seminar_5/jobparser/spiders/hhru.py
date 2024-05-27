import scrapy
from scrapy.http import HtmlResponse


class HhruSpider(scrapy.Spider):
    name = "hhru"
    allowed_domains = ["hh.ru"]
    start_urls = ["https://spb.hh.ru/search/vacancy?text=Руководитель+ит+отдела&from=suggest_post&salary=&resume=7d231f00ff0c7ddfbc0039ed1f32624b485472&ored_clusters=true&area=2&hhtmFrom=vacancy_search_list&hhtmFromLabel=vacancy_search_line"]

    def parse(self, response:HtmlResponse):
        # pass
        print(response.url, response.status)

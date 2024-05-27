import scrapy
from scrapy.http import HtmlResponse


class HhruSpider(scrapy.Spider):
    name = "hhru"
    allowed_domains = ["hh.ru"]
    start_urls = ["https://spb.hh.ru/search/vacancy?text=Руководитель+отдела+ИТ&salary=&ored_clusters=true&area=1&hhtmFrom=vacancy_search_list&hhtmFromLabel=vacancy_search_line"]
    def parse(self, response:HtmlResponse):
        # pass
        response.xpath("//span[@data-qa='serp-item__title']/@href")
        print(response.url, response.status)

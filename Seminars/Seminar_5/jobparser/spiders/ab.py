import scrapy
from scrapy.http import HtmlResponse

class AbSpider(scrapy.Spider):
    name = "ab"
    allowed_domains = ["avto-baki.ru"]
    start_urls = ["https://avto-baki.ru/the-fuel/"]
    ab_url = 'https://avto-baki.ru/'

    def parse(self, response:HtmlResponse):
        # pass
        links = response.xpath("//div[@class='ms2_product']//a[@class='h4']/@href").getall()
        for link in links:
            response.follow(ab_url + link, callback=self.tank_parse)

    def tank_parse(self, response:HtmlResponse):

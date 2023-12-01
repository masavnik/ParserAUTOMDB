import scrapy


class TiguanSpider(scrapy.Spider):
    name = "tiguan"
    allowed_domains = ["automdb.com"]
    start_urls = ["https://automdb.com/volkswagen/tiguan"]

    def parse(self, response):
        pass

import scrapy


class TiguanrSpider(scrapy.Spider):
    name = "tiguanR"
    allowed_domains = ["automdb.com"]
    start_urls = ["https://automdb.com/volkswagen/tiguan_r/i/group_offroad_5d"]

    def parse(self, response):
        pass

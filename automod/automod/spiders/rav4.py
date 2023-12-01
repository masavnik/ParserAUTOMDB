import scrapy


class Rav4Spider(scrapy.Spider):
    name = "rav4"
    allowed_domains = ["automdb.com"]
    start_urls = ["https://automdb.com/toyota/rav4"]

    def parse(self, response):
        pass

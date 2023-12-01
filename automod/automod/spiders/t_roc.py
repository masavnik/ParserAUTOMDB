import scrapy


class TRocSpider(scrapy.Spider):
    name = "t-roc"
    allowed_domains = ["automdb.com"]
    start_urls = ["https://automdb.com/volkswagen/t_roc_r"]

    def parse(self, response):
        pass

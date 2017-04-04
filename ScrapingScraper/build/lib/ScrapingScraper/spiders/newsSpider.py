from scrapy.spiders import Spider
from ScrapingScraper.items import ScrapingscraperItem
from scrapy.http    import Request

class MySpider(Spider):
    name            = "newsSpider"
    #only want news from 2017
    allowed_domains = ["www.kdnuggets.com/2017/"]
    #start crawling from news page
    start_urls      = ["http://www.kdnuggets.com/news/index.html"]

    def parse(self, response):
        for news in response.xpath('//a[contains(@href,"www.kdnuggets.com/2017/")]'):
            item = ScrapingscraperItem()
            item["title"] = news.xpath('text()').extract()
            item["url"] = news.xpath('@href').extract()
            if not item["title"] or not item["url"]:
                continue
            yield item

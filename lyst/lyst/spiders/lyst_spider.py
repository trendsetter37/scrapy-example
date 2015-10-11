from scrapy import Spider
from scrapy.selector import Selector
'''
product details xpath = '//div[@class="product-card"]/div[@class="product-details"]'
'''
class LystSpider(Spider):

    name = 'lyst'
    allowed_domains = ['http://www.lyst.com/']
    start_urls = ['http://www.lyst.com/new-today/']

    def parse(self, response):
        products = Selector(response).xpath('//div[@class="product-card"]')

        for product in products:
            pass #TODO

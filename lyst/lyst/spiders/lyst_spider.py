from scrapy import Spider
from scrapy.selector import Selector
from lyst.items import LystItem
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
            ''' pull designer, description, price, imgae_url, and image '''
            item = LystItem()

            item['designer'] = product.xpath(
                '/div[@class="product-details"]/a[@class="product-short-description"]/div[@class="product-designer"]/@data-designer'
            ).extract()[0]

            item['description'] = product.xpath(
                '/div[@class="product-details"]/a[@class="product-short-description"]/span/text()'
            ).extract()[0]

            item['price'] = product.xpath(
                '/div[@class="product-details"]/div[@class="product-price"]/span/text()'
            ).extract()[0] 
            pass #TODO

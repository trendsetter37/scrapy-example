from scrapy import Spider, Request
from scrapy.selector import Selector
from lyst.items import LystItem

'''
product details xpath = '//div[@class="product-card"]/div[@class="product-details"]'
'''
class LystSpider(Spider):

    name = 'lyst'
    allowed_domains = ['http://www.lyst.com/']
    start_urls = ['http://www.lyst.com/new-today/']
    cookies = {
        '__ssid':'eacf9496-15a3-40b4-b67c-d482f7d947ed',
        '_ga' : 'GA1.2.1819590536.1444660498',
        'analytics1': '4d4c96fa-8981-4b44-b45b-4a3ba14fcbbd:1:1:1444669394:16443ce3-1fb5-4fac-bcb9-7524f7dd0db1',
        'country': 'US',
        'sessionid':'ylvmjqpb5kwbpuqa4uwqhk5bihu7wgf5',
        'withfonts': '1'
    }

    def start_requests(self):
        for url in start_urls:
            request = Request(url, cookies=cookies, callback=self.parse)
            yield request

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

            item['image_url'] = product.xpath(
                '/div[@class="product-card-image-wrapper"]/a[@class="product-card-image-link"]/img/@src'
            ).extract()[0]

            yield item

import scrapy


class UfcSpider(scrapy.Spider):
    name = 'ufc'

    def start_requests(self):
        urls = [
            'https://www.ufc.com.br/rankings'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for categoria in response.css('.view-grouping-content'):
            yield{
                'categoria': categoria.css('h4::text').get(),
                'atletas' : categoria.css('a::text').getall()
            }

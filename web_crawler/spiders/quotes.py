# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader


from web_crawler.items import WebCrawlerItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']
    
    def parse(self, response):
        l = ItemLoader(item=WebCrawlerItem(),response=response)

        h1_tag = response.xpath('//*[@class="tag-item"]/a/text()').extract()
        tags = response.xpath("//h1/a/text()").extract_first()
        # yield {'H1_Tag':h1_tag, 'Tags':tags}
        l.add_value('h1_tag',h1_tag)
        l.add_value('tags',tags)
        return l.load_item()
        # container = response.xpath('//*[@class="quote"]')
        # for quote in container:
        #    text =  quote.xpath('.//*[@class="text"]/text()').extract_first()
        #    author =  quote.xpath('.//*[@class="author"]/text()').extract_first()
        #    keywords = quote.xpath('.//*[@class="keywords"]/@content').extract_first()
        #
        #    yield {
        #         'Text':text,
        #         'Author':author,
        #         'Key':keywords
        #    }
        #
        #    next_url = response.xpath('//*[@class="next"]/a/@href').extract_first()
        #    abs_next_url = response.urljoin(next_url)
        #    yield scrapy.Request(abs_next_url)
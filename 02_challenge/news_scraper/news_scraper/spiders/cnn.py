# -*- coding: utf-8 -*-
import json
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from news_scraper.items import NewsArticle

class CnnSpider(CrawlSpider):
    name = 'cnn'
    allowed_domains = ['edition.cnn.com']
    start_urls = ['https://edition.cnn.com/world']

    rules = [Rule(LinkExtractor(
        allow=r'\/2022\/\d{2}\/\d{2}'
        # allow=r'\/2022\/[0-9][0-9]\/[0-9][0-9]\/[a-zA-Z\-]+\/[a-zA-Z\-]+\/index.html'
        ),
        callback='parse_item', follow=True)]



    def parse_item(self, response):
        """
        url, source, title, description, date, author, text
        """
        article = NewsArticle()
        article['url'] = response.url
        article['source'] = 'cnn'
        article['title'] = response.xpath('//h1[@id="maincontent"]/text()').get()
        article['description'] = response.xpath('//meta[@name="description"]/@content').get()
        json_data = json.loads(response.xpath('//script[@type="application/ld+json"]/text()').get())
        article['date'] = response.xpath(
            '//meta[@property="article:published_time"]/@content').get()
        article['author'] = response.xpath('//meta[@name="author"]/@content').get()
        article['text'] = json_data['articleBody']
        return article

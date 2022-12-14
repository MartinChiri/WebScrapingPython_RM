# -*- coding: utf-8 -*-
import json
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from news_scraper.items import NewsArticle


class YahooSpider(CrawlSpider):
    name = 'yahoo'
    allowed_domains = ['news.yahoo.com']
    start_urls = ['http://news.yahoo.com/']

    rules = [Rule(LinkExtractor(
    allow=r'\.html$'
    ),
    callback='parse_item', follow=True)]

    def parse_item(self, response):
        """
        url, source, title, description, date, author, text
        """
        article = NewsArticle()
        article['url'] = response.url
        article['source'] = 'YaHoONews'
        json_data = json.loads(response.xpath(
            '//article[@role="article"]/script[@type="application/ld+json"]/text()').get())
        article['title'] = json_data['headline']
        article['description'] = json_data['description']
        article['date'] = json_data['datePublished']
        article['author'] = json_data['author']['name']
        article['text'] =  response.xpath(
            '//div[@class="caas-body"]/node()[not(self::button)]/text()').getall()
        return article

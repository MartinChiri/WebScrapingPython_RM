# -*- coding: utf-8 -*-
import json
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from news_scraper.items import NewsArticle


class ApnewsSpider(CrawlSpider):
    name = 'apnews'
    allowed_domains = ['apnews.com']
    start_urls = ['http://apnews.com/']

    rules = [Rule(LinkExtractor(
    allow=r'\/article\/'
    ),
    callback='parse_item', follow=True)]

    def parse_item(self, response):
        """
        url, source, title, description, date, author, text
        """
        article = NewsArticle()
        article['url'] = response.url
        article['source'] = 'APNews'
        article['title'] = response.xpath('//title/text()').get()
        article['description'] = response.xpath('//meta[@name="description"]/@content').get()
        json_data = json.loads(response.xpath('//script[@type="application/ld+json"]/text()').get())
        article['date'] = json_data['datePublished']
        article['author'] =json_data['author']
        article['text'] = response.xpath('//div[@class="Article"]/p/text()').getall()
        return article

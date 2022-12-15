# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider
from news_scraper.items import NewsArticle

def generate_start_urls():
    months = tuple(f'{n:02d}' for n in range(1,13))
    return ['https://cnn.com/sitemaps/article-{}-{}.xml'.format(year, month)
        for year in range(2012, 2023) for month in months]

class CnnSpider(CrawlSpider):

    name = 'cnn'
    allowed_domains = ['cnn.com']
    start_urls = generate_start_urls()

    def parse(self, response):
        article = NewsArticle()
        article['url'] = response.url
        article['count'] = response.text.count('<url>')
        return article

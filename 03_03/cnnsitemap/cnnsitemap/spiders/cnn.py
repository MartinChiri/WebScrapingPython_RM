# -*- coding: utf-8 -*-
import json
from scrapy.spiders import SitemapSpider
from cnnsitemap.items import NewsArticle


class CnnSpider(SitemapSpider):
    name = 'cnn'
    allowed_domains = ['edition.cnn.com']
    sitemap_urls = ['https://edition.cnn.com/sitemaps/article-2022-12.xml']


    def parse(self, response):
        """
        url, source, title, description, date, author, text
        """
        article = NewsArticle()
        article['url'] = response.url
        article['source'] = 'CNN'
        article['title'] = response.xpath('//h1[@id="maincontent"]/text()').get()
        article['description'] = response.xpath('//meta[@name="description"]/@content').get()
        article['date'] = response.xpath(
            '//meta[@property="article:published_time"]/@content').get()
        article['author'] = response.xpath('//meta[@name="author"]/@content').get()
        json_data = json.loads(response.xpath('//script[@type="application/ld+json"]/text()').get())
        article['text'] = json_data['articleBody']
        return article

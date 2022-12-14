# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsArticle(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    source = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    date = scrapy.Field()
    author = scrapy.Field()
    text = scrapy.Field()

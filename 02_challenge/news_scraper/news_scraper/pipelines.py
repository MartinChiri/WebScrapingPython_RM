# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from datetime import datetime

class NewsScraperPipeline:
    def process_item(self, item, spider):
        item['date'] = datetime.strptime(item['date'].split('T')[0], '%Y-%m-%d').date()
        # item.author = item.author.replace(', CNN', '')
        # item.text = [text.strip() for text in item.text]
        return item


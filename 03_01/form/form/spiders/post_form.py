# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest


class GetFormSpider(scrapy.Spider):
    name = 'post_form'
    allowed_domains = ['pythonscraping.com']


    def start_requests(self):
        names = ['Ricardo', 'Jesus', 'Bruno']
        quests = ['to see the grail', 'to learn Python', 'to scrape the Web']
        return [FormRequest('https://pythonscraping.com/linkedin/formAction2.php',
            formdata={'name':name, 'quest':quest, 'color':'blue'}, callback=self.parse
        ) for name, quest in zip(names, quests)]

    def parse(self, response):
        return {'text': response.xpath('//div[@class="wrapper"]/text()').get()}

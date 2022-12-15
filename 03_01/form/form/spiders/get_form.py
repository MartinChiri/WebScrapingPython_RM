# -*- coding: utf-8 -*-
import scrapy

def generate_start_urls():
    names = ['Ricardo', 'Jesus', 'Bruno']
    quests = ['to see the grail', 'to learn Python', 'to scrape the Web']
    return ['https://pythonscraping.com/linkedin/formAction.php?name={}&quest={}&color=red'.format(
        name,quest) for name, quest in zip(names, quests)
    ]


class GetFormSpider(scrapy.Spider):
    name = 'get_form'
    allowed_domains = ['pythonscraping.com']
    start_urls = generate_start_urls()

    def parse(self, response):
        return {'text': response.xpath('//div[@class="wrapper"]/text()').get()}

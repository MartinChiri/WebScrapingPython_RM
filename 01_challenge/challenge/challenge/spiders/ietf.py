# -*- coding: utf-8 -*-
import scrapy
import w3lib.html

class IetfSpider(scrapy.Spider):
    name = 'ietf'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['http://pythonscraping.com/linkedin/ietf.html']

    def parse(self, response):
        
        author_name = response.xpath('//span[@class="author-name"]/text()').get()
        author_company = response.xpath('//span[@class="author-company"]/text()').get()
        date = response.xpath('//span[@class="date"]/text()').get()
        title = response.xpath('//meta[@name="DC.Title"]/@content').get()
        address = response.xpath('//span[@class="address"]/text()').get()
        headings = response.xpath('//span[@class="subheading"]/text()').getall()
        text = w3lib.html.remove_tags(response.xpath('//div[@class="text"]').get())
        phone = response.xpath('//span[@class="phone"]/text()').get()
        email = response.xpath('//span[@class="email"]/text()').get()

        return {
                'author_name':author_name,
                'author_company':author_company,
                'date':date,
                'title': title,
                'address':address,
                'text':text,
                'headings':headings,
                'phone':phone,
                'email':email,
        }

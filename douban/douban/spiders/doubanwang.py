# -*- coding: utf-8 -*-
import scrapy


class DoubanwangSpider(scrapy.Spider):
    name = 'doubanwang'
    allowed_domains = ['douban.com']
    start_urls = ['https://accounts.douban.com/passport/login']

    def parse(self, response):
        pass

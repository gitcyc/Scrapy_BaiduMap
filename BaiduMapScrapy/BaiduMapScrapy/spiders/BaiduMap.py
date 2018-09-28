# -*- coding: utf-8 -*-
import scrapy


class BaidumapSpider(scrapy.Spider):
    name = 'BaiduMap'
    allowed_domains = ['map.baidu.com']
    start_urls = ['http://map.baidu.com/']

    def parse(self, response):
        pass

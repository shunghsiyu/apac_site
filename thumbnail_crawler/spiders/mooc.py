# -*- coding: utf-8 -*-
import scrapy


class MoocSpider(scrapy.Spider):
    name = 'mooc'
    allowed_domains = ['zh-tw.coursera.org']
    start_urls = ['http://zh-tw.coursera.org/']

    def parse(self, response):
        pass

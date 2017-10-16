# -*- coding: utf-8 -*-
import scrapy


class OcwSpider(scrapy.Spider):
    name = 'ocw'
    allowed_domains = ['ocw.aca.ntu.edu.tw']
    start_urls = ['http://ocw.aca.ntu.edu.tw/']

    def parse(self, response):
        pass

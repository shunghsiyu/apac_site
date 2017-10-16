# -*- coding: utf-8 -*-
import scrapy


class SpeechSpider(scrapy.Spider):
    name = 'speech'
    allowed_domains = ['speech.ntu.edu.tw']
    start_urls = ['http://speech.ntu.edu.tw/']

    def parse(self, response):
        pass

# -*- coding: utf-8 -*-
import scrapy

from ..items import ThumbnailCrawlerItem
from ..utils import url_list


class OcwSpider(scrapy.Spider):
    name = 'ocw'
    allowed_domains = ['ocw.aca.ntu.edu.tw']
    start_urls = ['http://ocw.aca.ntu.edu.tw/']

    def start_requests(self):
        for url in url_list(self):
            yield scrapy.Request(url)

    def parse(self, response):
        image_url = response.css('#course_pic img::attr(src)').extract_first()
        return ThumbnailCrawlerItem(image_urls=[image_url])


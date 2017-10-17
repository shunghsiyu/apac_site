# -*- coding: utf-8 -*-
import re

import scrapy

from ..items import ThumbnailCrawlerItem

class MoocSpider(scrapy.Spider):
    name = 'mooc'
    allowed_domains = ['zh-tw.coursera.org']
    banner_url_regex = re.compile(r'background-image:url\(https://\w+.cloudfront.net/api/utilities/v1/imageproxy/(https?://[^)]+)\);')

    def start_requests(self):
        return [scrapy.Request(url='https://zh-tw.coursera.org/learn/zhichang-suyang')]

    def parse(self, response):
        banner_style = response.css('#rendered-content div.body-container::attr(style)').extract_first()
        banner_url = self.banner_url(banner_style)
        return ThumbnailCrawlerItem(image_urls=[banner_url])

    def banner_url(self, style):
        return self.banner_url_regex.match(style).group(1)

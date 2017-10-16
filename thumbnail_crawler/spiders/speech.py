# -*- coding: utf-8 -*-
import re

import scrapy

from ..items import ThumbnailCrawlerItem

class SpeechSpider(scrapy.Spider):
    name = 'speech'
    allowed_domains = ['speech.ntu.edu.tw']
    youtube_id_regex = re.compile(r'https://www.youtube.com/embed/([^?]*)?.*')

    def start_requests(self):
        return [scrapy.Request(url='http://speech.ntu.edu.tw/ntuspeech/Video/id-1837')]

    def parse(self, response):
        youtube_url = response.css('#youtube_frame::attr(src)').extract_first()
        youtube_id = self.youtube_id(youtube_url)
        thumbnail_url = 'https://img.youtube.com/vi/{}/hqdefault.jpg'.format(youtube_id)
        return ThumbnailCrawlerItem(image_urls=[thumbnail_url])

    def youtube_id(self, url):
        return self.youtube_id_regex.match(url).group(1)


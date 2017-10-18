# -*- coding: utf-8 -*-
import re

import scrapy

from ..items import ThumbnailCrawlerItem
from ..utils import url_list


class SpeechSpider(scrapy.Spider):
    name = 'speech'
    allowed_domains = ['speech.ntu.edu.tw']
    youtube_id_regex = re.compile(r'https://www.youtube.com/embed/([^?]*)?.*')

    def start_requests(self):
        for url in url_list(self):
            yield scrapy.Request(url)

    def parse(self, response):
        youtube_url = response.css('#youtube_frame::attr(src)').extract_first()
        youtube_id = self.youtube_id(youtube_url)
        thumbnail_url = 'https://img.youtube.com/vi/{}/hqdefault.jpg'.format(youtube_id)
        title = ''.join(response.css('div.video-infoall h4.video-name *::text').extract()).strip()
        info = response.css('div.video-infoall p.video-info::text').extract_first().strip()
        return ThumbnailCrawlerItem(
            title=title,
            info=info,
            image_urls=[thumbnail_url],
        )

    def youtube_id(self, url):
        return self.youtube_id_regex.match(url).group(1)


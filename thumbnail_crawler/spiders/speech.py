# -*- coding: utf-8 -*-
import re

import scrapy

from ..items import ThumbnailCrawlerItem
from ..utils import url_list


split_regex = re.compile(r'、|,|，')


class SpeechSpider(scrapy.Spider):
    name = 'speech'
    allowed_domains = ['speech.ntu.edu.tw']
    youtube_id_regex = re.compile(r'https://www.youtube.com/embed/([^?]*)?.*')

    def start_requests(self):
        return list(url_list(self))

    def parse(self, response):
        youtube_url = response.css('#youtube_frame::attr(src)').extract_first()
        image_urls = []
        if youtube_url:
            youtube_id = self.youtube_id(youtube_url)
            thumbnail_url = 'https://img.youtube.com/vi/{}/hqdefault.jpg'.format(youtube_id)
            image_urls.append(thumbnail_url)
        title = ''.join(response.css('div.video-infoall h4.video-name *::text').extract()).strip()
        instructors = split_regex.split(response.css('#top div.video-who a::text').extract_first())
        info = response.css('div.video-infoall p.video-info::text').extract_first().strip()
        return ThumbnailCrawlerItem(
            title=title,
            instructors=[dict(name=instructor.strip(), department='', position='') for instructor in instructors],
            info=info,
            image_urls=image_urls,
            source=self.name,
            category=response.meta['category'],
            course_url=response.url,
        )

    def youtube_id(self, url):
        return self.youtube_id_regex.match(url).group(1)


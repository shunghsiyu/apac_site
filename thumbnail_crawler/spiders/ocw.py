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
        title = response.css('#course_description h2::text').extract_first()
        # Sometimes the `p` element is empty and doesn't contain any text
        # in such case using the `::text` selector will not select it
        info_element = response.css('#course_description > p')[0]
        info = '\n'.join(info_element.css('::text').extract())
        return ThumbnailCrawlerItem(
            title=title,
            info=info,
            image_urls=[image_url],
        )


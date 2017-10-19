# -*- coding: utf-8 -*-
import re

import scrapy

from ..items import ThumbnailCrawlerItem
from ..utils import url_list


class MoocSpider(scrapy.Spider):
    name = 'mooc'
    allowed_domains = ['zh-tw.coursera.org']
    banner_url_regex = re.compile(r'background-image:url\(https://\w+.cloudfront.net/api/utilities/v1/imageproxy/(https?://[^?]+)[^)]*\);')

    def start_requests(self):
        return list(url_list(self))

    def parse(self, response):
        banner_style = response.css('#rendered-content div.body-container::attr(style)').extract_first()
        banner_url = self.banner_url(banner_style)
        title = response.css('#rendered-content div.body-container h1.title::text').extract_first()
        instructors = [''.join(response.css('div.instructor-info p.instructor-name ::text').extract()[2:])]
        departments = response.css('div.instructor-info div.instructor-bio::text').extract()
        if departments:
            instructors = [instructor+' '+department for instructor, department in zip(instructors, departments)]
        info = response.css('div.about-section-wrapper div.content-inner p.course-description::text').extract_first()
        return ThumbnailCrawlerItem(
            title=title,
            instructors=instructors,
            info=info,
            image_urls=[banner_url],
            source=self.name,
            category=response.meta['category'],
            course_url=response.url,
        )

    def banner_url(self, style):
        return self.banner_url_regex.match(style).group(1)

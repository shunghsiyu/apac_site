# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ThumbnailCrawlerItem(scrapy.Item):
    title = scrapy.Field()
    info = scrapy.Field()
    image = scrapy.Field()
    image_urls = scrapy.Field()


# -*- coding: utf-8 -*-
import re

import scrapy


category_regex = re.compile(r'^\d\.(.+)：\r?\n')


def url_list(spider):
    input_file, allowed_domains = spider.input_file, spider.allowed_domains
    
    with open(input_file, mode='r') as f:
        category = None

        for line in f:
            category_match = category_regex.match(line)
            if category_match:
                category = category_match.group(1).strip()

            line_stripped = line.strip()
            if not line_stripped.startswith('http'):
                continue

            if any(domain in line_stripped for domain in allowed_domains):
                request = scrapy.Request(url=line_stripped)
                request.meta['category'] = category
                yield request
         

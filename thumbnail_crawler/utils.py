# -*- coding: utf-8 -*-

def url_list(spider):
    input_file, allowed_domains = spider.input_file, spider.allowed_domains
    
    with open(input_file, mode='r') as f:
        url_lines = [line for line in f if line.startswith('http')]
    correct_domain_lines = [
        line.strip() for line in url_lines if any(domain in line for domain in allowed_domains)
    ]

    return correct_domain_lines
         

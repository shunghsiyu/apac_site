#!/bin/bash
for spider in $(scrapy list); do scrapy crawl "$spider" -a input_file=urls.txt -o "output.jl"; done


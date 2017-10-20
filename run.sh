#!/bin/bash
export datetime="$(date -u '+%Y%m%dT%H%M%SZ')"
for spider in $(scrapy list);
    do scrapy crawl "$spider" -a input_file=urls.txt -s IMAGES_STORE="$(pwd)" -o "output-$datetime.jl";
done
python generate_yaml.py


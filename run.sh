#!/bin/bash
rm output.jl output.yml
for spider in $(scrapy list);
    do scrapy crawl "$spider" -a input_file=urls.txt -s IMAGES_STORE="$(pwd)" -o "output.jl";
done
python generate_yaml.py


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import jsonlines 
import csv


with jsonlines.open('output.jl', mode='r') as lines:
    data = list(lines)


def clean_data(row):
    row['instructors'] = '\n'.join(row['instructors'])
    row['image_urls'] = '\n'.join(row['image_urls'])
    return row


data = map(clean_data, data)


with open('output.csv', mode='w', newline='') as csvfile:
    fieldnames = ['title', 'instructors', 'info', 'image_urls', 'category', 'source', 'course_url']
    writer = csv.DictWriter(
        csvfile,
        fieldnames,
        extrasaction='ignore',
        quoting=csv.QUOTE_MINIMAL,
    )
    writer.writeheader()
    writer.writerows(data)


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import jsonlines 
import ruamel.yaml


class folded_unicode(str):

    @classmethod
    def to_yaml(cls, representer, node):
        return representer.represent_scalar('tag:yaml.org,2002:str', node, style='>')

    @staticmethod
    def represent_folded_unicode(dumper, data):
        scalar = raumel.yaml.SafeRepresenter(dumper, data)
        scalar.style = '>'
        return scalar


yaml = ruamel.yaml.YAML(pure=True)
yaml.register_class(folded_unicode)
yaml.default_flow_style = False
yaml.indent(mapping=2, sequence=4, offset=2)


with jsonlines.open('output-{}.jl'.format(os.environ['datetime']), mode='r') as lines:
    data = list(lines)


field_order = [
    'title',
    'instructors',
    'info',
    'images',
    'image_urls',
    'category',
    'source',
    'course_url',
]
def update_obj(obj):
    obj['info'] = folded_unicode(obj['info'])
    obj['images'] = list(order_mapping(image) for image in obj['images'])
    obj['instructors'] = list(order_mapping(instructor, ['name', 'position', 'department']) for instructor in obj['instructors'])
    return order_mapping(obj, field_order)


def order_mapping(old_map, order=None):
    new_map = ruamel.yaml.comments.CommentedMap()
    if order is None:
        order = sorted(old_map)
    for field in order:
        new_map[field] = old_map[field]
    return new_map
    

def data_keys(obj):
    return obj['source'], obj['category'], obj['course_url']
data = list(update_obj(obj) for obj in sorted(data, key=data_keys))


with open('output-{}.yml'.format(os.environ['datetime']), mode='w') as output_file:
    yaml.dump(data, output_file)


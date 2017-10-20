#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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


with jsonlines.open('output.jl', mode='r') as lines:
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
    mapping = ruamel.yaml.comments.CommentedMap()
    for field in field_order:
        mapping[field] = obj[field]
    return mapping


data = list(update_obj(obj) for obj in data)


with open('output.yml', mode='w') as output_file:
    yaml.dump(data, output_file)


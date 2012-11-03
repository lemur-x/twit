#!/usr/bin/env python
#coding: utf8

import urllib2
import re

patterns = {"a":"<a.*href=.*>.*</a>", "img":"<img.*src=.*>"}

def get_page(url):
    f = urllib2.urlopen(url)
    return f.read()

def search_tags(page, tag):
    pattern = patterns[tag]
    template = re.compile(pattern)
    lst = template.findall(page)
    return lst

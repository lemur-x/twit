#!/usr/bin/env python
#coding: utf8
import urllib2
import re

patterns = {"a":"<a.*href=.*>.*</a>", "img":"<img.*src=.*>"}

#TODO: url в параметре (запрос ввода) при запуске программы
#TODO: Найти все <img> теги
#TODO: Перенести get_page и search_tags в отдельный файл

def get_page(url):
    f = urllib2.urlopen(url)
    return f.read()

def search_tags(page, tag):
    pattern = patterns[tag]
    template = re.compile(pattern)
    lst = template.findall(page)
    return lst

def main():
    url = raw_input("Введите URL: ")
    tag = raw_input("Тег (%s):" %  patterns.keys())
    page = get_page(url)
    lst = search_tags(page, tag)
    for l in lst:
        print l

if __name__ == '__main__':
    main()
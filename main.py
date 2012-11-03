#!/usr/bin/env python
#coding: utf8
import urllib2
import re

#TODO: url в параметре (запрос ввода) при запуске программы
#TODO: Найти все <img> теги
#TODO: Перенести get_page и search_tags в отдельный файл

def get_page(url):
    f = urllib2.urlopen(url)
    return f.read()

def search_tags(page):
    pattern = "<a.*href=.*>.*</a>"
    template = re.compile(pattern)
    lst = template.findall(page)
    return lst

def main():
    url = 'https://twitter.com/search?q=linux&src=typd'
    page = get_page(url)
    lst = search_tags(page)
    print "count of <a> = %s" % len(lst)
    for l in lst:
        print l

if __name__ == '__main__':
    main()









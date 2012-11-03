#!/usr/bin/env python
#coding: utf8

from search import *

#TODO: url в параметре (запрос ввода) при запуске программы
#TODO: Найти все <img> теги
#TODO: Перенести get_page и search_tags в отдельный файл

def main():
    url = raw_input("Введите URL: ")
    tag = raw_input("Тег (%s):" %  patterns.keys())
    page = get_page(url)
    lst = search_tags(page, tag)
    for l in lst:
        print l

if __name__ == '__main__':
    main()
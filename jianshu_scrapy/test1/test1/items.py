# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Test1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    article = scrapy.Field()
    author = scrapy.Field()
    num_read = scrapy.Field()
    num_comment = scrapy.Field()
    uid = scrapy.Field()

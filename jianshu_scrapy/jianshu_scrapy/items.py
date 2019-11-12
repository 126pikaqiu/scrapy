# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JianshuScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    uid = scrapy.Field()
    nickname = scrapy.Field()
    num_following = scrapy.Field()
    num_follower = scrapy.Field()
    num_article = scrapy.Field()
    num_word = scrapy.Field()
    num_like = scrapy.Field()

class RelationItem(scrapy.Item):
    uid = scrapy.Field()
    follower = scrapy.Field()

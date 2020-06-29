# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class novelItem(scrapy.Item):
    ID = scrapy.Field()
    NAME = scrapy.Field()
    AUTHOR = scrapy.Field()
    TYPE = scrapy.Field()


class NovelspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    novelId = scrapy.Field()

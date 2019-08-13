# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrapyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 头像
    face = scrapy.Field()
    # 名字
    name = scrapy.Field()
    # 年龄
    age = scrapy.Field()
    # 内容
    content = scrapy.Field()
    # 好笑个数
    laugh = scrapy.Field()
    # 评论个数
    comment = scrapy.Field()

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Job51Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 职位名称
    jobname = scrapy.Field()
    # 公司名称
    company = scrapy.Field()
    # 工作地点
    place = scrapy.Field()
    # 薪资待遇
    salary = scrapy.Field()
    # 发布时间
    publish_time = scrapy.Field()


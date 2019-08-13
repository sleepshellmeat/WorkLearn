# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json
class Job51Pipeline(object):
    def open_spider(self, spider):
        self.fp = open('job51.txt', 'w', encoding='utf-8')

    def close_spider(self, spider):
        self.fp.close()

    def process_item(self, item, spider):
        dic = dict(item)
        string = json.dumps(dic, ensure_ascii=False)
        self.fp.write(string + '\n')
        return item

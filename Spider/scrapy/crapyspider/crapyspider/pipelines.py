# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json
class CrapyspiderPipeline(object):
    def open_spider(self, spider):
        self.fp = open('qiushi.txt', 'w', encoding='utf-8')

    def close_spider(self, spider):
        self.fp.close()

    def process_item(self, item, spider):
        # 因为传递过来的item为一个对象，需要转化为字典格式
        dic = dict(item)
        # 将字典转为为json格式的字符串，为了看懂中文so ensure_ascii=False
        string = json.dumps(dic, ensure_ascii=False)
        # 写入
        self.fp.write(string + '\n')
        return item

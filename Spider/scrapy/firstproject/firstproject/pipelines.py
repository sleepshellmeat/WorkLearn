# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json
class FirstprojectPipeline(object):
    """
    因为传递过来的item是一个生成器，所以process_item需要执行多次
    文件打开不能放在里面，可以放在__init__或者定义打开和关闭函数
    """
    # def __inite__(self):
    #     self.fp = open('qiushi.txt', 'w', encoding='utf-8')

    def open_spider(self, spider):
        self.fp = open('qiushi.txt', 'w', encoding='utf-8')

    def close_spider(self, spider):
        self.fp.close()

    # 处理item, item是yield过来的item, spider就是当前爬虫，不用动
    def process_item(self, item, spider):
        # 因为传递过来的item为一个对象，需要转化为字典格式
        dic = dict(item)
        # 将字典转为为json格式的字符串，为了看懂中文so ensure_ascii=False
        string = json.dumps(dic, ensure_ascii=False)
        # 写入
        self.fp.write(string + '\n')
        return item

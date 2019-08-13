# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
# Rule:规则类，写规则，当链接提取器提取了一批连接之后，会将这些链接扔给调度器，
#      调度器会调度这些链接，那么这些链接的相应来了之后，谁来处理这些响应。
from crapyspider.items import CrapyspiderItem


class QiubaiSpider(CrawlSpider):
    name = 'qiubai'
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    # rules是一个元组，里面写规则，规则起始就是Rule的一个对象
    lk = LinkExtractor(restrict_xpaths=('//ul[@class="pagination"]//a'))
    """
    参数1：链接提取器
    参数2：处理响应的回调函数，注意写法，函数名字符串。
           在CrawlSpider中parse函数有特定的作用不能重写。
           如果重写CrawlSpider失效，因为其作用就是提取链接。
    """
    rules = (
        Rule(lk, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # 获取内容的div
        all_div = response.xpath('//div[@id="content-left"]/div')
        # 遍历div列表
        for odiv in all_div:
            # 头像
            face = odiv.xpath('./div//img/@src').extract()[0]
            # 名字
            name = odiv.xpath('./div//h2/text()').extract()[0].strip(' \t\n')
            # 年龄
            try:
                age = odiv.xpath('./div/div/text()').extract()[0]
            except Exception as e:
                age = '没有年龄'
            # 内容
            lt = odiv.xpath('./a[1]//span//text()').extract()
            content = ''.join(lt).strip(' \t\n')
            # 好笑个数
            laugh = odiv.xpath('./div[@class="stats"]/span[1]/i/text()').extract()[0]
            # 评论个数
            comment = odiv.xpath('./div[@class="stats"]/span[2]//i/text()').extract()[0]

            # 创建一个FirstprojectItem的对象
            item = CrapyspiderItem()
            # 然后将以上解析过的数据存入到对象中
            for field in item.fields.keys():
                """
                此遍历把item里面全部的键遍历出来，键是在items.py里面定义好的
                第一次遍历为 item['face'] = eval(face)
                item['face']为取出对象中的face键
                eval(face)是将一个普通的字符串转化为变量，就对应上面解析好的face
                """
                item[field] = eval(field)
            '''
            最普通的方法可以一个一个写

            item['face'] = face
            item['name'] = name
            item['age'] = age
            item['content'] = content
            item['laugh'] = laugh
            item['comment'] = comment
            '''
            # 将item扔给引擎
            yield item

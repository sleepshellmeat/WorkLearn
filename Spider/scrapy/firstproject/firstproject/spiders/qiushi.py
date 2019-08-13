# -*- coding: utf-8 -*-
import scrapy
# 报红是pycharm的问题，能用
from scrapy.firstproject.firstproject.items import FirstprojectItem


class QiushiSpider(scrapy.Spider):
    name = 'qiushi'
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    page = 1
    url = 'https://www.qiushibaike.com/text/page/{}/'
    def parse(self, response):
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
            item = FirstprojectItem()
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

        # 接着发送请求，爬取其他页
        if self.page < 5:
            self.page += 1
            url = self.url.format(self.page)
            yield scrapy.Request(url=url, callback=self.parse)

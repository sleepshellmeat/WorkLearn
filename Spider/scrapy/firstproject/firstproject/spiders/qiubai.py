# -*- coding: utf-8 -*-
import scrapy


class QiubaiSpider(scrapy.Spider):
    # 爬虫的名字，在启动爬虫的时候要用到
    name = 'qiubai'
    # 允许的域名列表，如果列表为空，则默认位允许所有，一般最好不要为空
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        # 获取内容的div
        all_div = response.xpath('//div[@id="content-left"]/div')
        # 遍历div列表
        items = []
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
            item = {
                '头像': face,
                '名字': name,
                '年龄': age,
                '内容': content,
                '好笑个数': laugh,
                '评论个数': comment
            }
            items.append(item)
        return items
            # print('*' * 50)
            # print(content)
            # print('*' * 50)

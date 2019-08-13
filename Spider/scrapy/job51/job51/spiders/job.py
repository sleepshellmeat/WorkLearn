# -*- coding: utf-8 -*-
import scrapy
from job51.items import Job51Item

class JobSpider(scrapy.Spider):
    name = 'job'
    allowed_domains = ['http://search.51job.com/']
    start_urls = ['http://search.51job.com/list/170200,000000,0000,00,9,99,python,2,1.html?/']

    page = 1
    url = 'http://search.51job.com/list/170200,000000,0000,00,9,99,python,2,{}.html?/'

    def parse(self, response):
        div_list = response.xpath('//div[@class="dw_table"]/div[@class="el"]')
        for odiv in div_list:
            # 职位名称
            jobname = odiv.xpath('./p/span//@title').extract()[0]
            # 公司名称
            company = odiv.xpath('./span/a/@title').extract()[0]
            # 工作地点
            place = odiv.xpath('./span[@class="t3"]/text()').extract()[0]
            # 薪资待遇
            try:
                salary = odiv.xpath('./span[@class="t4"]/text()').extract()[0]
            except Exception as e:
                salary = ' '
            # 发布时间
            publish_time = odiv.xpath('./span[@class="t5"]/text()').extract()[0]
            item = Job51Item()
            for field in item.fields.keys():
                item[field] = eval(field)
            yield item

        if self.page < 5:
            self.page += 1
            url = self.url.format(self.page)
            # 在allowed_domains限制域名列表中不能有'http://'如果有，需要在下面加上dont_filter=True
            yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)

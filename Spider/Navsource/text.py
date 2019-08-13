import requests
from lxml import etree
import json
import time

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36}'
        }

url = 'http://www.navsource.org/archives/02idx.htm'
r = requests.get(url, headers=headers)
tree = etree.HTML(r.text)
href_list = tree.xpath('//center/table//tr/td/b/a/@href')
for href in href_list[:-2]:
        r = requests.get(url='http://www.navsource.org/archives/' + href, headers=headers)
        tree = etree.HTML(r.text)
        name = tree.xpath('/html/body//center/h1/b/font[contains(text(), "USS")]/text()')
        if len(tree.xpath('//tr/td/blockquote/b/ul//a[contains(text(), "Commanding")]/@href')) != 0:
                co_href = tree.xpath('//tr/td/blockquote/b/ul//a[contains(text(), "Commanding")]/@href')
        else:
                co_href = tree.xpath('//tr/td/blockquote/b/ul//li[contains(text(), "Commanding")]/a/@href')

        time.sleep(2)
        print(name)
        print(len(name))
        print('*' * 10)
        print(co_href)
        print(len(co_href))





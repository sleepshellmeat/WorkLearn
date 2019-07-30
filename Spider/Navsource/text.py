import requests
from lxml import etree

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36}'
        }

url = 'http://www.navsource.org/archives/01/puritan.htm'
r = requests.get(url, headers=headers)
# print(r.text)
tree = etree.HTML(r.text)
"""在xpathhelper里面能取，代码不能"""
tr_list = tree.xpath('//body/center[2]/center/table[1]//tr')[1:]
for tr in tr_list:
        co_name = tr.xpath('./td[2]//text()')[0].strip()
        print(co_name)
# 因为第一个tr不是想要的，try
"""
for tr in tr_list:
        try:
            co = tr.xpath('./td[2]//text()')[0].strip()
            time = tr.xpath('./td[3]/text()')[0].strip()
            item = {
                    '名字': co,
                    '任职时间': time
            }
            print(co)
            print(time)
            print(item)
        except:
               print('*' * 10)
        break
"""
"""名字和任职时间"""


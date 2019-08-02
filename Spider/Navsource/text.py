import requests
from lxml import etree
import json

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36}'
        }

url = 'http://www.navsource.org/archives/02idx.htm'
r = requests.get(url, headers=headers)
tree = etree.HTML(r.text)
href_list = tree.xpath('//center/table//tr/td/b/a/@href')
print(href_list)
print(len(href_list))
print(type(href_list))





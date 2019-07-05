"""
import hashlib


m = hashlib.md5()
m.update('rong is a good man'.encode('utf-8'))
if m.hexdigest() == '493747749d6d3ba6e656526e95c1a495':
    print('T')

herf = ''
hax = hashlib.sha1()
hax.update(herf.encode('utf-8'))
'aca2f414b7e8e682df15c6b160f6a96b4a923c07'

print(hax.hexdigest())



import requests
from lxml import etree
from time import sleep


url = 'http://www.uscarriers.net/cvn69.htm'

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36}'
    }


r = requests.get(url, headers=headers)
tree = etree.HTML(r.text)
a = tree.xpath('string(//tr/td/pre[@class="style2"])')
b = str(a)
print(b)
print(type(b))
"""

for i in range(0, 100, 20):
    print(i)

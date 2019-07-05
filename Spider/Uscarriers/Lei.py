import requests
from lxml import etree
from time import sleep

url = 'http://www.uscarriers.net/cvn.htm'
add_url = 'http://www.uscarriers.net/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36}'
}


# 定义一个解析类
class Parse():
    # 解析出各个航母的url
    def parse_url(self):
        r = requests.get(url, headers=headers)
        tree = etree.HTML(r.text)
        href_list = tree.xpath('//tr/td/div//a[contains(text(), "USS")]/@href')
        return href_list

    # 取出history的url
    def get_history_href(self):
        history_href_list = []
        for href in self.parse_url():
            r = requests.get(add_url + href, headers=headers)
            tree = etree.HTML(r.text)
            history_href = tree.xpath('//tr/td//a[contains(text(), "History")]/@href')[0]
            history_href_list.append(history_href)
        return history_href_list


# 定义一个爬取类
class Get():
    ...

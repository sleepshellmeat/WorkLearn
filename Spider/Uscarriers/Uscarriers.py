import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36}'
}

# 定义一个解析首页的函数，把CVN、DDG、CG、等解析后的url返回一个列表，以备二次解析。
def parse_navy_all():
    start_url = 'http://www.uscarriers.net/'
    r = requests.get(start_url, headers=headers)
    # 创建一个Xpath对象
    navy_all = etree.parse(r.text)
    # //tr//a[contains(text(),"USS")]/@href 解析二级页面的Xpath.
    all_href_list = navy_all.xpath('//tr//div[@align="center"]/a[1]/@href')
    return all_href_list

def parse_second(all_href_list):
    for href in all_href_list:
        r = requests.get(href, headers)
        second_all = etree.parse(r.text)
        second_href_list = second_all.xpath('//tr//a[contains(text(),"USS")]/@href')
        return second_href_list

def main():
    all_href_list = parse_navy_all()
    parse_second(all_href_list)

if __name__ == '__main__':
    main()
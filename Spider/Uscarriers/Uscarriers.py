import requests
from lxml import etree
from time import sleep

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36}'
}
start_url = 'http://www.uscarriers.net/'

# 定义一个解析首页的函数，把CVN、DDG、CG、等解析后的url返回一个列表，以备二次解析。
def parse_navy_all():
    r = requests.get(start_url, headers=headers)
    # 创建一个Xpath对象
    navy_all = etree.HTML(r.text)
    all_href_list = navy_all.xpath('//tr//div[@align="center"]/a[1]/@href')
    return all_href_list

def parse_second(all_href_list):
    for href in all_href_list:
        r = requests.get(start_url + href, headers)
        second_all = etree.HTML(r.text)
        second_href_list = second_all.xpath('//tr//a[contains(text(),"USS")]/@href')
        return second_href_list


def main():
    all_href_list = parse_navy_all()
    # parse_second(all_href_list)
    second_href_list = parse_second(all_href_list)
    for second_href in second_href_list:
        sep = '\n'
        fl = open('href.txt', 'w')
        fl.write(sep.join(second_href))
        sleep(2)
        fl.close()

if __name__ == '__main__':
    main()


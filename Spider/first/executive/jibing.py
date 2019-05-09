import requests
from lxml import etree
from time import sleep

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36}'
    }


def parse_url():
    url = 'http://jb.9939.com/'
    r = requests.get(url, headers=headers)
    tree = etree.HTML(r.text)
    href_list = tree.xpath('//div[@class="comdi nest newn"]/dl/dd/a/@href')
    return href_list


def parse_href(href_list):
    for href in href_list:
        r = requests.get(href, headers=headers)
        tree = etree.HTML(r.text)

        # 疾病名称
        illname = tree.xpath('//div[@class="widsp"]/b/text()')[0]

        # 别名
        str_list = tree.xpath('//ul[@class="niname"]/li[1]/p/a/@title')
        if len(str_list) < 1:
            othername = '暂无'
        else:
            othername = ''
            for str in str_list:
                othername += str + ', '
        print(othername)


def main():
    href_list = parse_url()
    parse_href(href_list)


if __name__ == '__main__':
    main()






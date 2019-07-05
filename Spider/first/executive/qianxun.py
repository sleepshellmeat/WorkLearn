import requests
from lxml import etree
from time import sleep


def parse_url(url, fp):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36}'
    }
    r = requests.get(url, headers=headers)
    tree = etree.HTML(r.text)
    content = tree.xpath("//div[@class='comment-item']//p/span/text()")
    for i in content:
        fp.write(i + '\n')
    sleep(5)

def pinjie(number):
        start_url = 'https://movie.douban.com/subject/1291561/comments?start={}&limit=20'.format(number)
        return start_url


def main():
    fp = open('pingjia.txt', 'w', encoding='utf-8')
    for number in range(0, 12000, 20):
        url = pinjie(number)
        a = parse_url(url, fp)
        print('已经爬取了%s条数据' % (number + 20))
    fp.close()


if __name__ == '__main__':
    main()
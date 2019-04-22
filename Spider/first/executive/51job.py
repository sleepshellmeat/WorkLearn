import requests
from time import sleep
from lxml import etree
from bs4 import BeautifulSoup


def pinjie_url(key_word, page, url):
    url = url.format(key_word, page)
    return url


def parse_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36}'
    }
    r = requests.get(url=url, headers=headers)
    r.encoding = 'gbk'
    # tree = etree.HTML(r.text)
    # div_list = tree.xpath('')
    soup = BeautifulSoup(r.text, 'lxml')
    div_list = soup.select('#resultList > .el')[1:]
    for odiv in div_list:
        jobname = odiv.select('.t1 > span > a')[0]['title']
        print(jobname)

def main():
    key_word = input("请输入要查询的职位：")
    start_page = int(input("请输入起始页码："))
    end_page = int(input("请输入结束页码："))

    url = 'https://search.51job.com/list/170200,000000,0000,00,9,99,{},2,{}.html?'
    for page in range(start_page, end_page + 1):
        url = pinjie_url(key_word, page, url)
        parse_url(url)


if __name__ == '__main__':
    main()

import requests
from time import sleep
from bs4 import BeautifulSoup


def pinjie_url(key_word, page, url):
    url = url.format(key_word, page)
    return url


def parse_url(url, fp):
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
        # 职位名称
        jobname = odiv.select('.t1 > span > a')[0]['title']
        # 公司名称
        company = odiv.select('.t2 > a')[0]['title']
        # 工作地点
        place = odiv.select('.t3')[0].string
        # 薪资待遇
        salary = odiv.select('.t4')[0].string
        # 发布时间
        publish_time = odiv.select('.t5')[0].string
        item = {
            '职位名称': jobname,
            '公司名称': company,
            '工作地点': place,
            '薪资待遇': salary,
            '发布时间': publish_time
        }
        string = str(item)
        fp.write(string + '\n')


def main():
    key_word = input("请输入要查询的职位：")
    start_page = int(input("请输入起始页码："))
    end_page = int(input("请输入结束页码："))

    url = 'https://search.51job.com/list/170200,000000,0000,00,9,99,{},2,{}.html?'
    fp = open('work.txt', 'w', encoding='utf-8')
    for page in range(start_page, end_page + 1):
        url = pinjie_url(key_word, page, url)
        parse_url(url, fp)
        print('正在爬取第%s页...' % page)
        sleep(5)
        print('结束爬取第%s页!' % page)
    fp.close()


if __name__ == '__main__':
    main()

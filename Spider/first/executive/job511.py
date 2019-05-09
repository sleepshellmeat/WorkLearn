import requests
from time import sleep
from bs4 import BeautifulSoup
from lxml import etree


headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36}'
    }

def pinjie_url(key_word, page, url):
    url = url.format(key_word, page)
    return url


def parse_url(url):
    r = requests.get(url=url, headers=headers)
    r.encoding = 'gbk'
    tree = etree.HTML(r.text)
    href_list = tree.xpath('//div/div[@id="resultList"]/div[@class="el"]/p/span/a/@href')
    # print(len(href_list))
    return href_list



def parse_href(href_list, fp):
    for href in href_list:
        r = requests.get(url=href, headers=headers)
        r.encoding = 'gbk'
        tree = etree.HTML(r.text)

        # 职位名称
        jobname = tree.xpath('//div[@class="cn"]/h1/@title')[0]

        # 公司名称
        company = tree.xpath('//div[@class="cn"]/p[@class="cname"]/a/@title')[0]

        # 薪资待遇
        try:
            salary = tree.xpath('//div[@class="cn"]/strong/text()')[0]
        except:
            salary = ''

        # 地区、工作经验、学历、招聘人数、发布时间
        alll = tree.xpath('//div[@class="cn"]/p[2]/@title')[0]
        llt = alll.split('|')
        lt = []
        for ltt in llt:
            a = ltt.strip()
            lt.append(a)
        if len(lt) > 4:
            area = lt[0]
            work_experience = lt[1]
            education = lt[2]
            number_people = lt[3]
            publish_time = lt[4]
        else:
            area = lt[0]
            work_experience = lt[1]
            education = ''
            number_people = lt[2]
            publish_time = lt[3]

        # 职位信息
        position = tree.xpath('//div[@class="tBorderTop_box"]/div[@class="bmsg job_msg inbox"]/p/text()')
        string = ''
        for i in position:
            string += i + ' '

        # 上班地址
        try:
            place = tree.xpath('//div[@class="tBorderTop_box"]/div[@class="bmsg inbox"]/p/text()')[1].strip()
        except:
            place = ' '

        # 公司信息
        company_info = tree.xpath('//div[@class="tBorderTop_box"]/div[@class="tmsg inbox"]/text()')
        strii = ''
        for c in company_info:
            strii += c.strip() + ' '


        item = {
            '职位名称': jobname,
            '公司名称': company,
            '地区':  area,
            '上班地址': place,
            '薪资': salary,
            '工作经验': work_experience,
            '学历': education,
            '招聘人数': number_people,
            '发布时间': publish_time,
            '职位信息': string,
            '公司信息': strii
        }
        stri = str(item)
        fp.write(stri + '\n')
        sleep(2)



"""
def save_to_mysql(db, item):
    cursor = db.cursor()
    sql = 'insert into job(jobname, company, place, salary, publish_time) value("%s","%s","%s","%s","%s")' % (
        item["职位名称"], item["公司名称"], item["工作地点"], item["薪资待遇"], item["发布时间"])
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
def content_db():
    db = pymysql.Connect(
        host='207.246.69.132',
        port='3306',
        user='root',
        password='222429',
        charset='utf8'
    )
    return db
"""


def main():
    key_word = input("请输入要查询的职位：")
    start_page = int(input("请输入起始页码："))
    end_page = int(input("请输入结束页码："))

    url = 'https://search.51job.com/list/170200,000000,0000,00,9,99,{},2,{}.html?'
    fp = open('work.txt', 'w', encoding='utf-8')
    # db = content_db()
    for page in range(start_page, end_page + 1):
        url = pinjie_url(key_word, page, url)
        href_list = parse_url(url)
        print('正在爬取第%s页...' % page)
        parse_href(href_list, fp)
        sleep(5)
        print('结束爬取第%s页!' % page)
    fp.close()
    # db.close()


if __name__ == '__main__':
    main()
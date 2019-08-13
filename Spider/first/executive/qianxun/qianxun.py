import requests
from lxml import etree
from time import sleep

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36}'
    }

# 创建一个Session会话，每次携带Session
s = requests.Session()

# 使用Fiddler抓取豆瓣电影的登陆接口
login_url = 'https://accounts.douban.com/j/mobile/login/basic'

# 创建一个表单
formdata = {
    'ck': '',
    'name': '13523570433',
    'password': 'wyz1195448923',
    'remember': 'false',
    'ticket': ''
}
# 发送携带Session的Post表单请求
r = s.post(login_url, headers=headers, data=formdata)


def parse_url(url, fp):
    r = s.get(url, headers=headers)
    tree = etree.HTML(r.text)
    content = tree.xpath("//div[@class='comment-item']//p/span/text()")
    for i in content:
        fp.write(i + '\n')
    sleep(8)

def pinjie(number):
        start_url = 'https://movie.douban.com/subject/1291561/comments?start={}&limit=20'.format(number)
        return start_url


def main():
    fp = open('pingjia.txt', 'w', encoding='utf-8')
    for number in range(0, 400, 20):
        url = pinjie(number)
        a = parse_url(url, fp)
        print('已经爬取了%s条数据' % (number + 20))
    fp.close()


if __name__ == '__main__':
    main()
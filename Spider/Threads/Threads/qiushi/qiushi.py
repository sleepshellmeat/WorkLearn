import requests
from lxml import etree
import threading
from threading import Lock
import time
from queue import Queue
import json

g_crawl = True
g_parse = True


class Crawl_Thread(threading.Thread):
    def __init__(self, name, page_queue, data_queue):
        super().__init__()
        self.name = name
        self.page_queue = page_queue
        self.data_queue = data_queue
        self.url = 'https://www.qiushibaike.com/text/page/{}/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36}'
        }

    def run(self):
        print('--%s--启动......' % self.name)
        while g_crawl:
            try:
                page = self.page_queue.get(False)
                r = requests.get(url=self.url.format(page), headers=self.headers)
                self.data_queue.put(r.text)
                time.sleep(2)
            except Exception as e:
                ...
        print('--%s--结束...' % self.name)

class Parse_Thread(threading.Thread):
    def __init__(self, name, data_queue, lock, fp):
        super().__init__()
        self.name = name
        self.data_queue = data_queue
        self.lock = lock
        self.fp = fp

    def run(self):
        print('--%s--启动......' % self.name)
        while g_parse:
            try:
                html = self.data_queue.get(False)
                self.parse(html)
                time.sleep(2)
            except Exception as e:
                ...
        print('--%s--结束...' % self.name)

    def parse(self, html):
        tree = etree.HTML(html)
        all_div = tree.xpath('//div[@id="content-left"]/div')
        # 遍历div列表
        for odiv in all_div:
            # 头像
            face = odiv.xpath('./div//img/@src')[0]
            # 名字
            name = odiv.xpath('./div//h2/text()')[0].strip(' \t\n')
            # 年龄
            try:
                age = odiv.xpath('./div/div/text()')[0]
            except Exception as e:
                age = '没有年龄'
            # 内容
            lt = odiv.xpath('./a[1]//span//text()')
            content = ''.join(lt).strip(' \t\n')
            # 好笑个数
            laugh = odiv.xpath('./div[@class="stats"]/span[1]/i/text()')[0]
            # 评论个数
            comment = odiv.xpath('./div[@class="stats"]/span[2]//i/text()')[0]

            items = {
                '头像': face,
                '名字': name,
                '年龄': age,
                '内容': content,
                '好笑个数': laugh,
                '评论个数': comment
            }
            string = json.dumps(items, ensure_ascii=False)
            if self.lock.acquire():
                self.fp.write(string + '\n')
                self.lock.release()


def create_queue(page):
    # 创建队列为10的页码队列和数据队列
    page_queue = Queue()
    data_queue = Queue()
    for i in range(1, page + 1):
        page_queue.put(i)
    return page_queue, data_queue


def main():
    page = int(input("请要爬取多少页："))
    page_queue, data_queue = create_queue(page)
    # 定于两个空列表，用来存放爬取线程和解析线程
    crawl_thread_list = []
    parse_thread_list = []

    lock = Lock()

    fp = open('qiushi.txt', 'w', encoding='utf-8')

    # 创建多线程列表
    crawl_name_list = ['爬取线程1', '爬取线程2', '爬取线程3']
    parse_name_list = ['解析线程1', '解析线程2', '解析线程3']

    # 将爬取多线程列表循环出来，然后挨个进行创建，也就是创建对象的过程
    for name in crawl_name_list:
        # 创建爬取线程对象,并将所需参数传入
        crawl_thread = Crawl_Thread(name, page_queue, data_queue)
        # 启动爬虫线程
        crawl_thread.start()
        # 将线程放入创建好的爬取空列表中
        crawl_thread_list.append(crawl_thread)

    # 同理创建解析线程
    for name in parse_name_list:
        parse_thread = Parse_Thread(name, data_queue, lock, fp)
        parse_thread.start()
        parse_thread_list.append(parse_thread)

    global g_crawl
    while 1:
        if page_queue.empty():
            g_crawl = False
            break

    for thread in crawl_thread_list:
        thread.join()

    global g_parse
    while 1:
        if data_queue.empty():
            g_parse = False
            break

    for thread in parse_thread_list:
        thread.join()

    fp.close()
    print('主进程和子近程全部结束')


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print('总共用时{}s'.format((end - start)))


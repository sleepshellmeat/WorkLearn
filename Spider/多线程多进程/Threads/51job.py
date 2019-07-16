import requests
from bs4 import BeautifulSoup
from time import sleep
import threading
from threading import Lock
from queue import Queue
import json


# 定义两个全局变量，用来标记采集和解析的退出条件
g_crawl = True
g_parse = True

class Crawl_Thread(threading.Thread):
    def __init__(self, name, page_queue, data_queue, key_word):
        # 这个在继承Thread后就是要指定的，目前还不知道为什么
        super().__init__()
        self.name = name
        self.page_queue = page_queue
        self.data_queue = data_queue
        self.key_word = key_word
        self.url = 'https://search.51job.com/list/170200,000000,0000,00,9,99,{},2,{}.html?'
        self.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36}'
        }

    def run(self):
        """如果不添加循环,这3个线程在每人请求到一条数据后就会结束
            从外部两个全局变量判断循环什么时候停止
        """
        print('--%s--启动......' % self.name)
        while g_crawl:
            # 为了防止队列等待，在get中添加一个False,只要从队列中请求不到就会报错
            try:
                # 通过传入的参数进行拼接url
                page = self.page_queue.get(False)
                url = self.url.format(self.key_word, page)
                # 对url发送请求
                r = requests.get(url, headers=self.headers)
                r.encoding = 'gbk'
                # 将请求后相应的页面数据put进数据队列
                """此处若使用r.text需要在上面指定gbk格式，但是r.content不需要"""
                self.data_queue.put(r.text)
                sleep(2)
            except Exception as e:
                ...
        print('--%s--结束...' % self.name)

class Parse_Thread(threading.Thread):
    def __init__(self, name, data_queue, fp, lock, page_queue):
        super().__init__()
        self.name = name
        self.data_queue = data_queue
        self.fp = fp
        self.lock = lock
        self.page_queue = page_queue

    def run(self):
        """如果不添加循环,这3个线程在每人请求到一条数据后就会结束
            从外部两个全局变量判断循环什么时候停止
        """
        print('--%s--启动......' % self.name)
        while g_parse:
            # 为了防止队列等待，在get中添加一个False,只要从队列中请求不到就会报错
            try:
                html = self.data_queue.get(False)
                self.parse(html)
                sleep(2)
            except Exception as e:
                ...
        print('--%s--结束...' % self.name)

    def parse(self, html):
        """对html进行解析"""
        soup = BeautifulSoup(html, 'lxml')
        jobinfo_list = soup.select('#resultList > .el')[1:]
        for jobinfo in jobinfo_list:
            jobname = jobinfo.select('.t1 a')[0].string.strip()
            company = jobinfo.select('.t2 a')[0].string
            workaddr = jobinfo.select('.t3')[0].string
            salary = jobinfo.select('.t4')[0].string
            buildtime = jobinfo.select('.t5')[0].string

            items = {
                'jobname': jobname,
                'company': company,
                'workaddr': workaddr,
                'salary': salary,
                'buildtime': buildtime,
            }
            # 将职典转换为json格式
            string = json.dumps(items, ensure_ascii=False)
            # 判断是否上锁，没上锁就开始写
            if self.lock.acquire():
                self.fp.write(string + '\n')
                # 写完之后释放锁
                self.lock.release()


def create_queue(start_page, end_page):
    # 创建队列为10的页码队列和数据队列
    page_queue = Queue(10)
    data_queue = Queue(10)
    # 在页码队列里面添加手动输入的页码
    for i in range(start_page, end_page + 1):
        page_queue.put(i)
    return page_queue, data_queue


def main():
    key_word = input("请输入要查询的职位：")
    start_page = int(input("请输入起始页码："))
    end_page = int(input("请输入结束页码："))
    # 创建页码队列和response队列
    page_queue, data_queue = create_queue(start_page, end_page)

    # 创建一个锁对象
    lock = Lock()

    # 打开需要读取的文件
    fp = open('job.txt', 'w', encoding='utf-8')

    # 定义两个空列表,用来装爬取和解析线程
    crawl_thread_list = []
    parse_thread_list = []

    # 创建多线程列表
    crawl_name_list = ['爬取线程1', '爬取线程2', '爬取线程3']
    parse_name_list = ['解析线程1', '解析线程2', '解析线程3']

    # 将爬取多线程列表循环出来，然后挨个进行创建，也就是创建对象的过程
    for name in crawl_name_list:
        # 创建爬取线程对象,并将所需参数传入
        crawl_thread = Crawl_Thread(name, page_queue, data_queue, key_word)
        # 启动线程
        crawl_thread.start()
        # 将线程添加到爬取线程列表里
        crawl_thread_list.append(crawl_thread)

    # 将解析多线程列表循环出来，然后挨个进行创建，也就是创建对象的过程
    for name in parse_name_list:
        # 创建解析线程对象,并将所需参数传入
        parse_thread = Parse_Thread(name, data_queue, fp, lock, page_queue)
        # 启动线程
        parse_thread.start()
        # 将线程添加到解析线程列表
        parse_thread_list.append(parse_thread)

    # 在这里一直判断  页码队列是否为空，如果为空，将g_crawl修改为False
    global g_crawl
    while 1:
        if page_queue.empty():
            g_crawl = False
            break

    # g_crawl = False 后爬取线程就可以停止了
    # 从爬取线程列表里面把爬取线程遍历出来进行挨个停止、
    for thread in crawl_thread_list:
        thread.join()

    # 爬取线程结束后，判断数据队列是否为空，如果为空，将g_parse修改为False
    global g_parse
    while 1:
        if data_queue.empty():
            g_parse = False
            break

    # 停止所有的解析线程
    for thread in parse_thread_list:
        thread.join()

    fp.close()

    print('主进程和子近程全部结束')


if __name__ == '__main__':
    main()
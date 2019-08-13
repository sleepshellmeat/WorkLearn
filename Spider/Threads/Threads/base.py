import requests
from lxml import etree
import threading
from threading import Lock
import time
from queue import Queue
import json


class Crawl_Thread(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        ...


class Parse_Thread(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        ...

    def parse(self):
        ...


def create_queue():
    # 创建队列为10的页码队列和数据队列
    page_queue = Queue(10)
    data_queue = Queue(10)
    # 爬取5页
    for i in range(5):
        page_queue.put(i)
    return page_queue, data_queue


def main():
    # 定于两个空列表，用来存放爬取线程和解析线程
    crawl_thread_list = []
    parse_thread_list = []

    # 创建多线程列表
    crawl_name_list = ['爬取线程1', '爬取线程2', '爬取线程3']
    parse_name_list = ['解析线程1', '解析线程2', '解析线程3']

    # 将爬取多线程列表循环出来，然后挨个进行创建，也就是创建对象的过程
    for name in crawl_name_list:
        # 创建爬取线程对象,并将所需参数传入
        crawl_thread = Crawl_Thread(name)
        # 启动爬虫线程
        crawl_thread.start()
        # 将线程放入创建好的爬取空列表中
        crawl_thread_list.append(crawl_thread)

    # 同理创建解析线程
    for name in parse_name_list:
        parse_thread = Parse_Thread(name)
        parse_thread.start()
        parse_thread_list.append(parse_thread)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print('总共用时{}s'.format((end - start)))


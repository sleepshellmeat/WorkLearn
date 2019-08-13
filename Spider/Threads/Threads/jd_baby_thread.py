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
        self.headers = {
        'Referer': 'https://item.jd.com/1263013576.html',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36}'
        }
        self.url = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv5413&productId=1263013576&score=0&sortType=5&page=%s&pageSize=10&isShadowSku=0&fold=1'
        self.name = name
        self.page_queue = page_queue
        self.data_queue = data_queue

    def run(self):
        """
        添加循环，让线程不停止，一直到爬虫结束
        """
        print('--%s--启动......' % self.name)
        while g_crawl:
            # try:
                page = self.page_queue.get()
                print('取出{}页'.format(page))
                r = requests.get(self.url.format(page), headers=self.headers)
                print(r.text)
                self.data_queue.put(r.text)
                print(self.data_queue.qsize())
                print('添加代码执行完成')
            # except Exception as e:
            #     print('爬取错误。。。')
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
        print('--%s--启动......' % self.name)
        while g_parse:
            # try:
                html = self.data_queue.get()
                print(html)
                json_str = html[26:-2]
                json_obj = json.loads(json_str)
                json_comments = json_obj['comments']
                for json_comment in json_comments:
                    string = json.loads(json_comment['content'], ensure_ascii=False)
                    if self.lock.acquire():
                        self.fp.write(string + '\n')
                        self.lock.release()

            # except Exception as e:
            #     print('解析错误。。。')
        print('--%s--结束...' % self.name)




def create_queue(all_page):
    page_queue = Queue(10)
    data_queue = Queue(10)
    # 循环出要爬取的页码放在页码队列
    for i in range(all_page):
        page_queue.put(i)
        # print('添加页面队列')
    return page_queue, data_queue

def main():
    all_page = int(input('请输入要爬取多少页：'))

    # 创建页码队列和数据队列
    page_queue, data_queue = create_queue(all_page)

    # 定于两个空列表，用来存放爬取线程和解析线程
    crawl_thread_list = []
    parse_thread_list = []

    # 创建一个锁
    lock = Lock()

    # 打开要读取的文件
    fp = open('jd_baby_thread.txt', 'w', encoding='utf-8')

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
        time.sleep(1)
        parse_thread = Parse_Thread(name, data_queue, fp, lock, page_queue)
        parse_thread.start()
        parse_thread_list.append(parse_thread)

    # 判断页码队列是否为空，如为空将g_crawl改为False
    global g_crawl
    while 1:
        if page_queue.empty():
            g_crawl = False
            break

    # 然后关闭爬取线程
    for thread in crawl_thread_list:
        thread.join()

    # 判断数据队列是否为空，如为空将g_crawl改为False
    global g_parse
    while 1:
        if data_queue.empty():
            g_parse = False
            break

    # 关闭所有的解析线程
    for thread in parse_thread_list:
        thread.join()

    fp.close()
    print('主线程子线程全部停止。')


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print('总共用时{}s'.format((end - start)))


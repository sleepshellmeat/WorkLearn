import json
import threading
import time
from queue import Queue
from threading import Lock
import requests
from bs4 import BeautifulSoup

# 定义两个全局变量，用来标记采集和解析的退出条件
g_crawl = True
g_parse = True

def create_queue():
    page_queue = Queue(10)
    data_queue = Queue(10)
    for i in range(1, 11):
        page_queue.put(i)

    return page_queue,data_queue


class Crawl_Thread(threading.Thread):
    def __init__(self,name,page_queue,data_queue):
        super().__init__()
        self.name = name
        self.page_queue = page_queue
        self.data_queue = data_queue
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
        }
        self.url = 'https://search.51job.com/list/020000,000000,0000,00,9,99,c,2,{}.html'

    def run(self):
        print('--%s--启动......' % self.name)
        while g_crawl:
            try:
                page = self.page_queue.get(False)
                url = self.url.format(page)
                r = requests.get(url=url,headers=self.headers)
                self.data_queue.put(r.content)
                time.sleep(2)
            except Exception as e:
                pass
            
        print('--%s--结束...' % self.name)

class Parse_Thread(threading.Thread):
    def __init__(self,name,data_queue,fp,lock,page_queue):
        super().__init__()
        self.name = name
        self.data_queue = data_queue
        self.fp = fp
        self.lock = lock
        self.page_queue = page_queue

    def run(self):
        print('--%s--启动......' % self.name)
        while g_parse:
            try:
                html = self.data_queue.get(False)
                self.parse(html)
                time.sleep(2)
            except Exception as e:
                pass
            
        print('--%s--结束...' % self.name)

    def parse(self,html):
        soup = BeautifulSoup(html,'lxml')
        jobinfo_list = soup.select('#resultList > .el')[1:]
        # print(jobinfo_list)
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
            #将数据转化成json数据
            string = json.dumps(items,ensure_ascii=False)
            if self.lock.acquire():
                self.fp.write(string + '\n')
                self.lock.release()




def main():
    #创建页码队列和response信息队列
    page_queue,data_queue = create_queue()
    crawl_thread_list = []
    parse_thread_list = []

    lock = Lock()
    #打开要写入的文件
    fp = open('job.txt','w',encoding='utf8')
    crawl_name_list = ['采集线程1','采集线程2','采集线程3']
    parse_name_list = ['解析线程1','解析线程2','解析线程3']
    for name in crawl_name_list:
        #创建线程
        crawl_thread = Crawl_Thread(name,page_queue,data_queue)
        crawl_thread.start()
        crawl_thread_list.append(crawl_thread)
    for name in parse_name_list:
        parse_thread = Parse_Thread(name,data_queue,fp,lock,page_queue)
        parse_thread.start()
        parse_thread_list.append(parse_thread)

    # 在这里一直判断  页码队列是否为空，如果为空，将g_crawl修改为False
    global g_crawl
    while 1:
        if page_queue.empty():
            g_crawl = False
            break
    # 页码队列为空，采集线程结束，数据队列为空，这时候解析线程就可以退出了

    for thread in crawl_thread_list:
        thread.join()

    # 只要走到这，就代表所有的采集线程都已经结束
    global g_parse
    while 1:
        if data_queue.empty():
            g_parse = False
            break
    # 让主线程等待所有的解析线程结束
    for thread in parse_thread_list:
        thread.join()

    fp.close()


    print('主进程子进程全部结束')



if __name__ == '__main__':
    main()
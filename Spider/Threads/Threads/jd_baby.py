import requests, time, json, os, random, jieba
from multiprocessing import Process, Pool


text_name = 'jd_comment.txt'
def spider_comment(page):
    headers = {
        'Referer': 'https://item.jd.com/1263013576.html',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36}'
    }
    url = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv5413&productId=1263013576&score=0&sortType=5&page=%s&pageSize=10&isShadowSku=0&fold=1' % page
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
    except:
        print('爬取失败')

    json_str = r.text[26:-2]
    json_obj = json.loads(json_str)
    json_comments = json_obj['comments']
    # print(json_comments)
    for json_comment in json_comments:
        # a+ 这里是追加模式进行写入
        with open(text_name, 'a+', encoding='utf-8') as fp:
            fp.write(json_comment['content'] + '\n')



def main():
    # 写入数据之前先清空数据
    if os.path.exists(text_name):
        os.remove(text_name)
    print('开始爬取。。。')
    for i in range(5):
        spider_comment(i)
    time.sleep(random.random() * 10)
    print('第{}页爬取结束！。。。'.format(i + 1))


def content_time(main):
    start = time.time()
    main()
    end = time.time()
    print('爬取完成!总共用时{}s'.format((end - start)))


if __name__ == '__main__':
    content_time(main)
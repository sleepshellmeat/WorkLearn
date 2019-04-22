import urllib.request
from bs4 import BeautifulSoup
import time
# import pymysql
# import pymongo

def handle_request(keyword, page, url):
	# 拼接url
	url = url.format(keyword, page)
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
	}
	request = urllib.request.Request(url=url, headers=headers)
	return request

def parse_content(content,fp):
	# 生成soup对象
	soup = BeautifulSoup(content, 'lxml')
	# 先找到所有的包含工作的div
	# div_list = soup.find_all('div', class_='el')[1:]
	div_list = soup.select('#resultList > .el')[1:]
	# print(len(div_list))
	# 遍历每一个div，依次获取工作的每一个详细信息
	for odiv in div_list:
		# 职位名称
		jobname = odiv.select('.t1 > span > a')[0]['title']
		# 公司名称
		company = odiv.select('.t2 > a')[0]['title']
		# 工作地点
		area = odiv.select('.t3')[0].string
		# 薪资
		salary = odiv.select('.t4')[0].string
		# 发布时间
		publish_time = odiv.select('.t5')[0].string
		# print(salary, publish_time)
		# 放入一个字典中
		item = {
			'职位名称': jobname,
			'公司名称': company,
			'工作地点': area,
			'薪资': salary,
			'发布时间': publish_time
		}
		string = str(item)
		fp.write(string + '\n')
		# save_to_mysql(db, item)


def main():
    keyword = input('请输入要搜索的关键字-')
    start_page = int(input('请输入起始页码-'))
    end_page = int(input('请输入结束页码-'))
    url = 'https://search.51job.com/list/020000,000000,0000,00,9,99,{},2,{}.html'
    fp = open('work.txt', 'w', encoding='utf8')
    for page in range(start_page, end_page + 1):
        print('正在爬取--第%s页--......' % page)
        # 拼接url生成请求对象
        request = handle_request(keyword, page, url)
        # 发送请求，得到响应内容
        content = urllib.request.urlopen(request).read().decode('gbk')
        # 解析函数
        parse_content(content, fp)
        print('结束爬取--第%s页--...' % page)
        time.sleep(3)
    fp.close()

# db = connect_db()
#client = connect_mongodb()
# 选择mongodb的数据库
#db = client.job51
# 选择mongodb的集合
#col = db.job

# 循环，依次爬取每一页的数据

# db.close()
#client.close()
if __name__ == '__main__':
    main()



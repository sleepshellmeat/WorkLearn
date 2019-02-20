import requests

"""
url = 'http://www.baidu.com/'
r = requests.get(url)
r.encoding = 'utf8'
print(r.text)
"""

'''
# 带参数的get
url = 'https://www.baidu.com/s?'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36}'
data = {
    'wd': '中国'
}
r = requests.get(url, headers=headers, params=data)

print(r.content)
'''

url = 'http://www.baidu.com'
r = requests.get(url)
# 把结果保存到文件中
with open('baidu.html', 'wb') as fp:
    fp.write(r.content)
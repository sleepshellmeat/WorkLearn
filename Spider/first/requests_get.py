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
    'User-Agent': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
}
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
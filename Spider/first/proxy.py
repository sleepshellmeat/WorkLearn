import requests

url = 'https://www.google.com/'
# url = 'https://www.baidu.com/s?wd=ip'

headers = {'User-Agent': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'}
# 这是自定义一个代理池，格式就是字典。
proxy = {
    'http': 'http://207.246.119.165:2019'
}
# 使用代理获取网页，方法是proxies,proxy的复数形式。
r = requests.get(url, headers=headers, proxies=proxy)
# 把google首页保存带当前文件夹。
with open('google.html', 'wb') as fp:
    fp.write(r.content)
# print(r.text)


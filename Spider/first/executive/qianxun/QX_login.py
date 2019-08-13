import requests

# 创建一个Session会话，每次携带Session
s = requests.Session()

# 使用Fiddler抓取豆瓣电影的登陆接口
login_url = 'https://accounts.douban.com/j/mobile/login/basic'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36}'
}

formdata = {
    'ck': '',
    'name': '13523570433',
    'password': 'wyz1195448923',
    'remember': 'false',
    'ticket': ''
}

# 发送携带Session的Post表单请求
r = s.post(login_url, headers=headers, data=formdata)

# 发送get请求
get_url = 'https://www.douban.com/people/199326412/'
r1 = s.get(get_url, headers=headers)
print(r1.cookies)



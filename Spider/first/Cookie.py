import requests

# 创建一个会话，每次携带Session
s = requests.Session()
# 使用fiddler抓取人人网的login接口
post_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=201913116663 '

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36}'
}
# 手动登录时fiddler抓取的form表单
formdata = {
    'email': '15560167595',
    'icode': '',
    'origURL': 'http://www.renren.com/home',
    'domain': 'renren.com',
    'key_id': '1',
    'captcha_type': 'web_login',
    'password': '9ad61a4c32be84de2f50c327c04948ad7320f5993b7de4d0da14e7b50d65a47f',
    'rkey':	'afb46a40efe492c657ce0a05b507bd73',
    'f': 'http%3A%2F%2Fwww.renren.com%2F968673720'
}
# 携带Session的post请求
r = s.post(post_url, headers=headers, data=formdata)
# print(r.text)
# 个人信息的页面链接
get_url = "http://www.renren.com/968673720/profile"
# 携带Session的get请求
r1 = s.get(get_url, headers=headers)
print(r1.text)

"""ck	
	"""
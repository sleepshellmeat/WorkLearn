import requests

# 抓的是必应翻译的接口
url = "http://cn.bing.com/ttranslationlookup?&IG=359B370513634614AA9FA0A3E04992A1&IID=translator.5038.10"
# 定制请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36}'
}
# 定制form表单数据
formdata = {
    'from': 'en',
    'to': 'zh-CHS',
    'text': 'lion'
}
r = requests.post(url, headers=headers, data=formdata)
# 得到json格式数据
print(r.json())

import requests

url = "http://www.uscarriers.net/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36}'
}

r = requests.get(url, headers=headers)

# print(r.text)
with open('Uscarriers.html', 'wb') as fp:
    fp.write(r.content)
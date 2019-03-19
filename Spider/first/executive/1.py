import requests

url = "http://www.uscarriers.net/cvn69history.htm"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36}'
}

# proxy = {
#     'http': 'http://207.246.119.165:2019'
# }

r = requests.get(url, headers=headers)

print(r.text)
# with open('CVN-69history.html', 'wb') as fp:
#     fp.write(r.content)
import requests

url = 'https://cn.bing.com/ttranslationlookup?&IG=B491CC90C81D4B84BAB5B5E5356B372E&IID=translator.5038.5'

form = {
    "from": "en",
    "to": "zh-CHS",
    "text": "lion"
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36}'
}

r = requests.post(url, headers=headers, data=form)

print(r.text)
import requests
from lxml import etree
from time import sleep
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36}',
    'Referer': 'http://www.zzsggzy.com/'
}
start_url = 'http://www.zzsggzy.com/chanquan/cqlist.html'

def get_href():
    r = requests.get(start_url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    # href_list = tree.xpath('//td[@class="ewb-td3"]//a/@href')
    print(soup)

# def main():
#     href_list = get_href()
#     print(href_list)
#
#
# if __name__ == '__main__':
#     main()
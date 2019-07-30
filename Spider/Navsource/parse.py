import requests
from lxml import etree
import time
import random
import json

"""
battleships 战列舰
aircraft_carriers 航空母舰
escort_carriers 航母护航舰
cruisers 巡洋舰
destroyers 驱逐舰
DE_FFG_LCS 页面中有驱逐舰护航舰、护卫舰、濒海战斗舰
submarines 各种潜艇
service_sessels 服务船
sealift 海上补给船
amphibiors 两栖舰
mine_warfare 扫雷船
patrol_vessels 巡逻船
yard_district 页面中有干船坞、拖船、油水驳船、轻型驳船（自力和非自力推进）、等
civilian_vessels 民用船
steam_sailIndex 海军更早的时候使用的蒸汽船和帆船
rigid_airships 飞艇
army_ships 陆军船只
"""
url_dict = {
    'battleships': 'http://www.navsource.org/archives/01idx.htm',
    'aircraft_carriers': 'http://www.navsource.org/archives/02idx.htm',
    'escort_carriers': 'http://www.navsource.org/archives/03idx.htm',
    'cruisers': 'http://www.navsource.org/archives/04idx.htm',
    'destroyers': 'http://www.navsource.org/archives/05idx.htm',
    'DE_FFG_LCS': 'http://www.navsource.org/archives/06idx.htm',
    'submarines': 'http://www.navsource.org/archives/subidx.htm',
    'service_sessels': 'http://www.navsource.org/archives/auxidx.htm',
    'sealift': 'http://www.navsource.org/archives/09/80idx.htm',
    'amphibiors': 'http://www.navsource.org/archives/phibidx.htm',
    'mine_warfare': 'http://www.navsource.org/archives/mineidx.htm',
    'patrol_vessels': 'http://www.navsource.org/archives/patidx.htm',
    'yard_district': 'http://www.navsource.org/archives/ydidx.htm',
    'civilian_vessels': 'http://www.navsource.org/archives/12/17idx.htm',
    'steam_sailIndex': 'http://www.navsource.org/archives/09/86/86idx.htm',
    'rigid_airships': 'http://www.navsource.org/archives/02/99/0299idx.htm',
    'army_ships': 'http://www.navsource.org/archives/armyidx.htm'
}

headers = {
        'Referer': 'http://www.navsource.org/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36}'
        }


class Parse():
    ...


class Parse_Battleships():
    def __init__(self):
        ...

    def get_first_href(self):
        r = requests.get(url=url_dict['battleships'], headers=headers)
        tree = etree.HTML(r.text)
        # 此页面第一个不取，用列表切片去除
        href_list = tree.xpath('//center/table/tbody/tr[2]/td/b/a/@href')[1:5]
        return href_list

    def get_second_href(self):
        # 取出二级页面的href
        second_href_list = []
        for href in self.get_first_href():
            r = requests.get(href, headers=headers)
            tree = etree.HTML(r.text)
            href_list =tree.xpath('//tr/td/b/a/@href')
            for href in href_list:
                second_href_list.append(href)
                # break
            time.sleep(random.random() * 5)
            # break
        return second_href_list

    def get_info(self):
        # try:
            fp = open('battleships.txt', 'w', encoding='utf-8')
            for href in self.get_second_href():
                r = requests.get(href, headers=headers)
                tree = etree.HTML(r.text)
                name = tree.xpath('/html/body/center/h1/b/font/text()')[0]
                info_list = tree.xpath('/html/body/text()')
                info = ' '.join(info_list)
                # 先取出存放CO的tr标签列表
                tr_list = tree.xpath('//body/center[2]/center/table[1]//tr')[1:]
                if len(tr_list) == 0:
                    item = {
                        '名称': name,
                        '信息': info,
                    }
                    string = json.dumps(item, ensure_ascii=False)
                    fp.write(string + '\n')
                    print('成功写入一个111')

                else:
                    # 遍历出来挨个进行取
                    lt = []
                    for tr in tr_list:
                        co_name = tr.xpath('./td[2]//text()')[0].strip()
                        time = tr.xpath('./td[3]/text()')[0].strip()
                        it = {
                            '舰长': co_name,
                            '任职时间': time
                        }
                        lt.append(it)
                    item = {
                        '名称': name,
                        '信息': info,
                        'CO': lt
                    }
                    string = json.dumps(item, ensure_ascii=False)
                    fp.write(string + '\n')
                    print('成功写入一个222')
            fp.close()
        # except:
        #     print('又他妈错了。。。')











import requests
from lxml import etree

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

class Parse_Battleships():
    def __init__(self):
        ...







import requests
from lxml import etree
from time import sleep


url = 'http://www.uscarriers.net/cvn.htm'
add_url = 'http://www.uscarriers.net/'

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36}'
    }


def parse_url():
    r = requests.get(url, headers=headers)
    tree = etree.HTML(r.text)
    href_list = tree.xpath('//tr/td/div//a[contains(text(), "USS")]/@href')
    return href_list


def get_history_href(href_list):
    history_href_list = []
    for href in href_list:
        r = requests.get(add_url + href, headers=headers)
        tree = etree.HTML(r.text)
        history_href = tree.xpath('//tr/td//a[contains(text(), "History")]/@href')[0]
        history_href_list.append(history_href)
    return history_href_list


def get_info(href_list, fp):
    for href in href_list:
        r = requests.get(add_url + href, headers=headers)
        tree = etree.HTML(r.text)
        # 取出所有的参数
        all_canshu = tree.xpath('string(//tr/td/pre[@class="style2"])')
        # 清洗数据
        clear_canshu1 = all_canshu.split('\n')
        clear_canshu = ' '.join(clear_canshu1).strip().split('           ')

        # 这里判断一下是否是福特级，因格式不一样，所以福特级需要单独的简单存放
        if href == 'cvn78.htm':
            item = {
                '名称': 'USS GERALD R. FORD CVN 78',
                '参数': ' '.join(clear_canshu)
            }
            print('正在爬取USS GERALD R. FORD CVN 78')
        else:
            lt = [i for i in clear_canshu if i.find(':') == -1 or i.startswith(' -') == True]

            # 名称
            name_list = tree.xpath('//tr/td/div//span/text()')
            name = '  '.join(name_list)

            # 建造时间
            Keel_Laid = clear_canshu[0].split(':')[1]


            # 命名时间
            Christened = clear_canshu[1].split(':')[1]


            # 服役时间
            Commissioned = clear_canshu[2].split(':')[1]


            # 建造商
            Builder = clear_canshu[3].split(':')[1]


            # 推进系统
            Propulsion_system = clear_canshu[4].split(':')[1] + lt[0]


            # 总长度
            Lengths = clear_canshu[6].split(':')[1]


            # 飞行甲板宽度
            Flight_Deck_Width = clear_canshu[7].split(':')[1]


            # 飞行甲板面积
            Flight_Deck_Area = clear_canshu[8].split(':')[1]

            # 船宽
            Beam = clear_canshu[9].split(':')[1]


            # 吃水深度
            Draft = clear_canshu[10].split(':')[1]


            # 排水量
            Displacement = clear_canshu[11].split(':')[1]


            # 速度
            Speed = clear_canshu[12].split(':')[1]


            # 飞机信息
            Planes = clear_canshu[13].split(':')[1]


            # 人员
            Crew = clear_canshu[14].split(':', 1)[1]


            # 武器
            Armament = ' '.join(lt[1:])


            # 母港
            Homeport = clear_canshu[-1].split(':')[1]


            item = {
                '名称': name,
                '建造时间': Keel_Laid,
                '命名时间': Christened,
                '服役时间': Commissioned,
                '建造商': Builder,
                '推进系统': Propulsion_system,
                '总长度': Lengths,
                '飞行甲板宽度': Flight_Deck_Width,
                '飞行甲板面积': Flight_Deck_Area,
                '船宽': Beam,
                '吃水深度': Draft,
                '排水量': Displacement,
                '速度': Speed,
                '飞机信息': Planes,
                '人员': Crew,
                '武器': Armament,
                '母港': Homeport
            }
            print('正在爬取%s' % name)
        string = str(item)
        fp.write(string + '\n')
        sleep(10)


def main():
    href_list = parse_url()
    history_href_list = get_history_href(href_list)
    fp = open('CVN.txt', 'w', encoding='utf-8')
    get_info(href_list, fp)

    fp.close()


if __name__ == '__main__':
    main()
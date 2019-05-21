import requests
from lxml import etree
from time import sleep

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36}'
    }


def parse_url():
    url = 'http://jb.9939.com/'
    r = requests.get(url, headers=headers)
    tree = etree.HTML(r.text)
    href_list = tree.xpath('//div[@class="comdi nest newn"]/dl/dd/a/@href')
    return href_list


def parse_href(href_list):
    for href in href_list:
        r = requests.get(href, headers=headers)
        tree = etree.HTML(r.text)

        # 疾病名称
        try:
            illname = tree.xpath('//div[@class="widsp"]/b/text()')[0]
        except:
            illname = ' '

        # 别名
        str_list = tree.xpath('//ul[@class="niname"]/li[1]/p/a/@title')
        if len(str_list) < 1:
            othername = '暂无'
        else:
            othername = ','.join(str_list)

            # othername = ''
            # for str in str_list:
            #     othername += str + ', '

        # 发病部位
        try:
            ill_site = tree.xpath('//ul[@class="niname"]/li[2]/p[1]/a/@title')[0]
        except:
            ill_site = ''

        # 挂号科室
        try:
            department_list = tree.xpath('//ul[@class="niname"]/li[2]/p[2]/a/text()')
            if len(department_list) > 1:
                department = ','.join(department_list)

                # department = ''
                # for i in department_list:
                #     department += i + ','
            else:
                department = department_list[0]
        except:
            department = '暂无'

        # 传播方式
        infect_way_list = tree.xpath('//ul[@class="niname"]/li[3]/p[1]/text()')
        if len(infect_way_list) > 1:
            infect_way = ','.join(infect_way_list)

            # infect_way = ''
            # for i in infect_way_list:
            #     infect_way += i + ''
        else:
            try:
                infect_way = infect_way_list[0]
            except:
                infect_way = ' '

        # 易感人群
        try:
            susceptible = tree.xpath('//ul[@class="niname"]/li[3]/p[2]/text()')[0]
        except:
            susceptible = ' '

        # 典型症状
        try:
            symptom_list = tree.xpath('//ul[@class="niname"]/li[4]/p[1]/a/@title')
            if len(symptom_list) > 1:
                symptom = ','.join(symptom_list)
            else:
                symptom = symptom_list[0]

        except:
            symptom = '暂无'

        # 治疗方法
        try:
            therapy = tree.xpath('//ul[@class="niname"]/li[4]/p[2]/text()')[0]
        except:
            therapy = ' '
        print(illname, ill_site, department, susceptible, therapy)
        sleep(3)


def main():
    href_list = parse_url()
    parse_href(href_list)


if __name__ == '__main__':
    main()






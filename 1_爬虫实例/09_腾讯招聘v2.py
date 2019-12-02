#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import etree
import requests
import xlwt
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
}
info_base_url = 'https://hr.tencent.com/'
# 1. 创建 列表页链接  https://hr.tencent.com/position.php?lid=&tid=&keywords=python&start=10#a
def creat_url_list(maxNum):
    base_url = "https://hr.tencent.com/position.php?lid=&tid=&keywords=python&start={0}#a"
    url_list = []
    for x in range(0, maxNum, 10):
        url_list.append(base_url.format(x))
    return url_list

# 2. 请求列表页 拿去 职位链接、职位名称 https://hr.tencent.com/position.php?lid=&tid=&keywords=python&start=10#a
def request_list(url_list):
    print('请求链接-列表：{0} ...'.format(url_list))
    info_url_list=[]
    for item in url_list:
        resp = requests.get(item, headers=headers)
        html = etree.HTML(resp.text)
        info_urls=html.xpath("//td[@class ='l square']/a/@href")
        for item in info_urls:
            info_url_list.append(str(info_base_url)+str(item))
    return info_url_list
# 4. 请求 详情页 拿去 html
def request_info_page(url):
    print('请求链接-详情：{0} ...'.format(url))
    resp2 = requests.get(url, headers=headers)
    html2 = etree.HTML(resp2.text)
    title_list = html2.xpath("//*[@id='sharetitle']/text()")
    place_list = html2.xpath('//tr[2]/td[1]/text()')
    position_list = html2.xpath('//tr[2]/td[2]/text()')
    num_list = html2.xpath('//tr[2]/td[3]/text()')
    duty_list = html2.xpath('//tr[3]//ul[@class="squareli"]/li/text()')
    requir_list = html2.xpath('//tr[4]//ul[@class="squareli"]/li/text()')
    for title,place,position,num,duty,requir in zip( title_list,place_list,position_list,num_list,duty_list,requir_list):
        info_data = {
            '职位': title,
            '工作地点': place,
            '职位类别': position,
            '招聘人数': num,
            '工作职责': duty,
            '工作要求': requir
        }
    return info_data

# 6. 打印 info_list
def run():
    info_list = []
    url_list = creat_url_list(maxNum=30)
    info_url_list = request_list(url_list)
    for item in info_url_list:
        info_list.append(request_info_page(url=item))
    return info_list
    # print(info_url_list)

    # print(info_list)
    # for item in info_list:
    #     print(item)

def save_info(info_list):
    workbook = xlwt.Workbook(encoding='utf-8')
    first_sheet = workbook.add_sheet('电影天堂')
    row = ["职位", "工作地点", "职位类别", "招聘人数", "工作职责", "工作要求"]
    for h in range(len(row)):
        first_sheet.write(0, h, row[h])
    a = 1
    for aa in info_list:
        b = 0
        for data in aa:
            first_sheet.write(a, b, aa[data])
            b += 1
        a += 1
    workbook.save('7' + ".xls")

if __name__ == '__main__':
    info_list = run()
    save_info(info_list)


#     workbook = xlwt.Workbook(encoding='utf-8')
#     first_sheet = workbook.add_sheet('电影天堂')
#     row = ["职位", "工作地点", "职位类别", "招聘人数", "工作职责", "工作要求"]
#
#     for h in range(len(row)):
#         first_sheet.write(0, h, row[h])
#
#     a = 1
#     for aa in lists:
#         b = 0
#         for data in aa:
#             first_sheet.write(a, b, aa[data])
#             b += 1
#         a += 1
# workbook.save('7' + ".xls")








#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import etree
import requests
import xlwt

# url = "https://hr.tencent.com/position.php?lid=&tid=&keywords=python"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
}



infos = []

def get_info_url(url):
    resp = requests.get(url, headers=headers)
    html = etree.HTML(resp.text)
    ul = html.xpath("//td[@class ='l square']/a/@href")
    return ul
def get_info(url):
    lists = []
    resp2 = requests.get(url,headers=headers)
    html2 = etree.HTML(resp2.text)
    title_list = html2.xpath("//*[@id='sharetitle']/text()")
    place_list = html2.xpath('//tr[2]/td[1]/text()')
    position_list = html2.xpath('//tr[2]/td[2]/text()')
    num_list = html2.xpath('//tr[2]/td[3]/text()')
    duty_list = html2.xpath('//tr[3]//ul[@class="squareli"]/li/text()')
    requir_list = html2.xpath('//tr[4]//ul[@class="squareli"]/li/text()')
    for title, place, position, num, duty, requir in zip(title_list, place_list, position_list, num_list, duty_list,requir_list):
        list = {
            '职位': title,
            '工作地点': place,
            '职位类别': position,
            '招聘人数': num,
            '工作职责': duty,
            '工作要求': requir
        }
    lists.append(list)

    print(lists)
    return lists

def get_page():
    detail_url = 'https://hr.tencent.com/'
    base_url = "https://hr.tencent.com/position.php?lid=&tid=&keywords=python&start={0}#a"
    # infos = []
    for x in range(0,20,10):
        url = base_url.format(x)
        print(url)
        urllist = get_info_url(url)
        print(urllist)
        for urllists in urllist:
            info = get_info(detail_url + urllists)
            infos.append(info)
            #print(infos)


# info_list=[]
# # 1. 创建 列表页链接  https://hr.tencent.com/position.php?lid=&tid=&keywords=python&start=10#a
# def creat_url_list(maxNum):
#     base_url = "https://hr.tencent.com/position.php?lid=&tid=&keywords=python&start={0}#a"
#     infos = []
#     for x in range(0, maxNum, 10):
#         url = base_url.format(x)
#         urllist = get_info_url(url)
#         for urllists in urllist:
#             info = get_info(detail_url + urllists)
#             infos.append(info)
#     return infos
#
#
# # 2. 请求列表页 拿去 职位链接、职位名称 https://hr.tencent.com/position.php?lid=&tid=&keywords=python&start=10#a
# def request_list(url):
#     pass
#
# # 3. 组装详情页 链接  https://hr.tencent.com/position_detail.php?id=49769&keywords=python&tid=0&lid=0
# def format_info_url(url):
#     pass
#
# # 4. 请求 详情页 拿去 html
# def request_info_page(url):
#     pass
#
# # 5. 解析详情html  储存打 info_list
# def format_info_html(html):
#     pass
#
# # 6. 打印 info_list
# def print_info_list():
#     request_list_path=creat_url_list(maxNum=30)
#     print(request_list_path)
#
#     parint(info_list)


if __name__ == '__main__':
    get_page()
    workbook = xlwt.Workbook(encoding='utf-8')
    first_sheet = workbook.add_sheet('电影天堂')
    row = ["职位", "工作地点", "职位类别", "招聘人数", "工作职责", "工作要求"]
    for h in range(len(row)):
        first_sheet.write(0, h, row[h])
    a = 1
    for aa in infos:
        b = 0
        for data in aa:
            for item in data:
                print(data)
                first_sheet.write(a, b, aa[data])
            b += 1
        a += 1
    workbook.save('8' + ".xls")








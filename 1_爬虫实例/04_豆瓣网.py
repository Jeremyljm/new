#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from lxml import etree
import xlwt


# 1.将目标网站的页面抓取下来

headers = {
    "urser-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
    "Referer": "https://movie.douban.com/"
}
movies = []

def get_info(url):
    resp = requests.get(url,headers=headers)
    # print(resp.text)
    # resp.text ：返回的是一个经过解码后的字符串，是str（unicode）类型
    # resp.content：返回的是一个原生的字符串，就是网页上直接抓取下来的，没有经过处理的字符串，是bytes类型
    text = resp.text

    html = etree.HTML(text)
    ul = html.xpath("//ul[@class= 'lists']")[0]
    li = ul.xpath("./li")
    for lis in li:
        # print(etree.tostring(lis,encoding='utf-8').decode('utf-8'))
        title = lis.xpath("@data-title")
        score = lis.xpath("@data-score")
        duration = lis.xpath("@data-duration")
        region = lis.xpath("@data-region")
        director = lis.xpath("@data-director")
        actors = lis.xpath("@data-actors")
        pic = lis.xpath(".//img/@src")
        movie = {
            'title': title,
            'score': score,
            'duration': duration,
            'region': region,
            'director': director,
            'actors': actors,
            'pic': pic
        }
        movies.append(movie)



if __name__ == '__main__':
    get_info('https://movie.douban.com/cinema/nowplaying/hangzhou/')
    workbook = xlwt.Workbook(encoding='utf-8')
    first_sheet = workbook.add_sheet('douban')
    row = ["电影名称", "评分", "时长", "产地" ,"导演" ,"演员","图片"]

    for h in range(len(row)):
        first_sheet.write(0, h, row[h])

    a = 1
    for list in movies:
        b = 0
        for data in list:
            first_sheet.write(a,b,list[data])
            b+=1
        a+=1

workbook.save('5' + ".xls")
# for j, job in enumerate(movies):
#     for i in range(len(row)):
#         first_sheet.write(j + 1, i, list(movies.values())[i])







# 2.将抓取的下来的数据根据一定的规则进行提取
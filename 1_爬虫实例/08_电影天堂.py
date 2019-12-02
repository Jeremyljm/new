#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import etree
import requests
import xlwt

base_domain = 'http://www.ygdy8.net'
headers = {
    "urser-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
}

aa = []
def get_detail_urls(url):
    resp = requests.get(url, headers=headers)
    text = resp.text
    html = etree.HTML(text)
    detail_urls = html.xpath("//table[@class= 'tbspan']//a/@href")
    detail_urls = map(lambda url:base_domain+url,detail_urls)
    return detail_urls

def parse_detail_page(url):
    movie = {}
    resp = requests.get(url, headers=headers)
    text = resp.content.decode('gbk')
    html = etree.HTML(text)
    title = html.xpath("//div[@class = 'title_all']//font[@color= '#07519a']/text()")[0]
    print(title)
    movie['title'] = title
    zoomE = html.xpath("//div[@id = 'Zoom']")[0]
    imgs = zoomE.xpath(".//img/@src")
    cover = imgs[0]
    screenshot = imgs[1]
    movie['cover'] = cover
    movie['screenshot'] = screenshot
    aa.append(movie)

    def parse_info(info, rule):
        return info.replace(rule,"").strip()

    infos = zoomE.xpath(".//text()")
    for index, info in enumerate(infos):
        print(info)
        print(index)
        print('='*30)
        if info.startswith("◎年　　代"):
            info = parse_info(info, "◎年　　代")
            movie['year'] = info
        elif info.startswith("◎产　　地"):
            info = parse_info(info, "◎产　　地")
            movie['country'] = info
        elif info.startswith("◎类　　别"):
            info = parse_info(info, "◎类　　别")
            movie['category'] = info
        elif info.startswith("◎豆瓣评分"):
            info = parse_info(info, "◎豆瓣评分")
            movie['douban_rating'] = info
        elif info.startswith("◎片　　长"):
            info = parse_info(info, "◎片　　长")
            movie['duration'] = info
        elif info.startswith("◎导　　演"):
            info = parse_info(info, "◎导　　演")
            movie['director'] = info
        elif info.startswith("◎主　　演"):
            info = parse_info(info, "◎主　　演")
            actors = [info]
            for x in range(index+1,len(infos)):
                actor = infos[x].strip()
                if actor.startswith("◎"):
                    break
                actors.append(actor)
            movie['actors'] = actors
        elif info.startswith("◎简　　介"):
            info = parse_info(info, "◎简　　介")
            for x in range(index+1,len(infos)):
                profile = infos[x].strip()
                movie["profile"] = profile
    download_url = html.xpath("//td[@bgcolor='#fdfddf']/a/@href")[0]
    movie['download_url'] = download_url
    return movie


def spider():
    base_url = "http://www.ygdy8.net/html/gndy/dyzz/list_23_{0}.html"
    movies = []
    for x in range(1,3):
        url = base_url.format(x)
        detail_urls = get_detail_urls(url)
        for detail_url in detail_urls:
            movie = parse_detail_page(detail_url)
            movies.append(movie)
            print(movie)


if __name__ == '__main__':
    spider()

    workbook = xlwt.Workbook(encoding='utf-8')
    first_sheet = workbook.add_sheet('电影天堂')
    row = ["电影名称", "图片链接1","图片链接2","年代", "产地", "类别","豆瓣评分" ,"片长","导演", "主演", "简介","下载链接"]

    for h in range(len(row)):
        first_sheet.write(0, h, row[h])

    a = 1
    for list in aa:
        b = 0
        for data in list:
            first_sheet.write(a, b, list[data])
            b += 1
        a += 1
workbook.save('6' + ".xls")






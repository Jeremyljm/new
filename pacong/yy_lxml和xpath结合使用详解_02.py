#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import etree
# 1. 获取所有的tr标签
# 2. 获取第二个tr标签
# 3. 获取所有的class等于even的标签
# 4. 获取所有a标签的href属性
# 5. 获取所有的职位信息（纯文本）


parser = etree.HTMLParser(encoding='utf-8')
html = etree.parse("lagou.html",parser=parser)

# 1. 获取所有的tr标签
# trs = html.xpath("//h3")
# for tr in trs:
#     print(etree.tostring(tr,encoding='utf-8').decode("utf-8"))

# 2. 获取第二个tr标签
# trs = html.xpath("//dd[2]")[0]
# print(etree.tostring(trs,encoding='utf-8').decode("utf-8"))

# 3. 获取所有的class等于even的标签
# trs = html.xpath("//span[@class='money']")
# for tr in trs:
#   print(etree.tostring(tr,encoding='utf-8').decode("utf-8"))

# 4. 获取所有a标签的href属性
# list = html.xpath("//a/@href")
# for a in list:
#     print(a)

# 5. 获取所有的职位信息（纯文本）
trs = html.xpath("//li[@class]")
for tr in trs:
    href = tr.xpath(".//a[@class='position_link']")
    print(href,encoding='utf-8')

# >1 获取某个标签的属性
"""
href = html.xpath("//a/@href")
"""
# 2> 获取文本是通过xpath中的text()函数
"""
address = tr.("./td[4]/text()")[0]
"""
# 3> 在某个标签下，在执行xpath函数，获取这个标签的子孙元素，那么应该在斜杠之前加一个点，代表是在当前元素下获取：
"""
address = tr.("./td[4]/text()")[0]
"""
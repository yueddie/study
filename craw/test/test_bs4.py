# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_bs4
   Description :
   Author :       eddie
   date：          2021/1/19
-------------------------------------------------
   Change Activity:
                   2021/1/19:
-------------------------------------------------
"""
__author__ = 'eddie'

import re

from bs4 import BeautifulSoup

file = open("baidu.html", "rb")
html = file.read()
bs = BeautifulSoup(html, "html.parser")
# print(bs.a)
# print(type(bs.title))
# print(bs.title.string)
# print(type(bs.title.string))
# print(type(bs))
# print(type(bs.a.string))
# print(bs.title.string)
# bs4.Tag 拿到html标签里的内容，但是只能拿到第一个标签里的内容
# bs4.NavigableString就时标签里的字符串
# bs4.BeautifulSoup表示整个文档
# bs4 Comment 是一个特殊的NavigableString，就是不包含注释的符号
# Tag.contents 属性可以将tag子节点以列表方式返回 如:bs.head.contents,更多内容查看文档


# 文档搜索


# 1.find_all()
# 字符串过滤：会查找与字符完全匹配的结果
# t_list = bs.find_all("a")

# 整则表达式搜索：使用search()方法来匹配内容
# t_list = bs.find_all(re.compile("a"))
# print(t_list)


# 方法搜索 ：传入函数，根据函数要求搜索
# def name_is(tag):
#     return tag.has_attr("name")
#
# t_list = bs.find_all(name_is)
# print(t_list)

# 2. **kwargs
# t_list = bs.find_all(id="head")
# t_list = bs.find_all(class_=True)


# 3.text参数
# t_list=bs.find_all(text=["新闻","贴吧"])
# t_list=bs.find_all(text=re.compile("\d"))

# 4 limit参数
# t_list = bs.find_all('a', limit=3)  # 限制搜索个数
#
# for i in t_list:
#     print(i)

# # CSS 选择器
# t_list=bs.select("title") # 通过标签来查找
# t_list = bs.select(".mnav")  # 根据类名查找
# t_list = bs.select("#uq")  # 通过id查查找
# t_list = bs.select("a[class='bri']")  # 通过属性查找
t_list = bs.select("head>title")  # 通过子标签查找

for i in t_list:
    print(i)
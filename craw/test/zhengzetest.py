# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     zhengzetest
   Description :
   Author :       eddie
   date：          2021/1/20
-------------------------------------------------
   Change Activity:
                   2021/1/20:
-------------------------------------------------
"""
__author__ = 'eddie'

# 正则表达式：判断字符串是否符合一定的标准
import re

# 创建模式对象
# pat = re.compile("AA")  # 此处AA是正则表达式
# m = pat.search("asdAAC")  # search是需要比对的内容,仅匹配第一次出现的查找


# 没事模式对象
# m = re.search("AA", "AAAD")
# print(m.span())

# #findall
# m=re.findall("a", "adafasfgas")  # 前面字符串是正则，后面是需要校验的字符串，找到字符串中所有符合规则的字符
# m = re.findall("[a-z]+", "adafaAs，fgas")
# ['adafa', 's', 'fgas']
# print(m)
# #sub
# m = re.sub("[a-z]", "A","BBasfacCCC")
# print(m)
# 建议再正则表达式中和被比较的字符串中加入r，这样不用担心转义字符的影响
str = 'asdad<a href="https://movie.douban.com/subject/1292052/">dad'
finLink = re.compile(r'<a href="(.*)">')
data = re.search(finLink, str)
print(data.group())

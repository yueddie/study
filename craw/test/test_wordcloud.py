# -*- coding: utf-8 -*-
import jieba  # 分词
import numpy as np  # 矩阵运行
from matplotlib import pyplot as plt  # 绘图,数据可视化
from wordcloud import wordcloud  # 词云
from PIL import Image  # 图形处理
import sqlite3

conn = sqlite3.connect('movie250.db')
cs = conn.cursor()
sql = 'select introduction from movie'
data = cs.execute(sql)
text = ''
for item in data:
    text = text + item[0]
    # print(item)
# print(text)
cs.close()
conn.close()
cuts = jieba.cut(text)
strs = ' '.join(cuts)
print(len(strs))
img = Image.open(r'kk2.jpeg')
img_arr = np.array(img)  # 将图片转成数组
wc = wordcloud.WordCloud(background_color='white',
                         mask=img_arr,
                         font_path='msyh.ttc'
                         ).generate_from_text(strs)

fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off')
plt.show()

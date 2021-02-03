# -*- coding: utf-8 -*-
import urllib.request, urllib.error
from bs4 import BeautifulSoup
import re
import xlwt
import sqlite3

__author__ = 'eddie'

finLink = re.compile(r'<a href="(.*?)">')
finImageSrc = re.compile(r'<img.*src="(.*?)"', re.S)
findTitle = re.compile(r'<span class="title">(.*)</span>')
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
findJuge = re.compile(r'<span>(\d*)人评价</span>')
finInq = re.compile(r'<span class="inq">(.*)</span>')
finBd = re.compile(r'<p class="">(.*?)</p>', re.S)


def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 1 爬取网页
    date_list = get_date(baseurl)
    print('爬取分析数据')
    get_date(baseurl)
    print("爬取分析数据结束")
    # 3 保存数据
    # save_path = '.\\dou_ban_top_250.xls'
    # save_date(date_list, save_path)
    # 4 保存到数据库
    db_path = 'movie250.db'
    save_data_to_db(db_path, date_list)


# 1 爬取网页
def get_date(base_url):
    date_list = []
    # 逐一爬取网页
    for i in range(0, 10):
        url = base_url + str(i * 25)
        html = ask_url(url)
        # 2 逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_='item'):
            data = []
            item = str(item)
            link = re.findall(finLink, item)[0]  # 影片详细链接
            data.append(link)
            img_src = re.findall(finImageSrc, item)[0]  # 影片图片地址
            data.append(img_src)
            title = re.findall(findTitle, item)  # 影片名字，只要中文和外文
            if len(title) == 2:
                ctitle = title[0]
                data.append(ctitle)
                otitle = title[1].replace("/", "")
                data.append(otitle.strip())
            else:
                data.append(title[0])
                data.append(" ")  # 留空
            rating = re.findall(findRating, item)[0]  # 评分
            data.append(rating)
            juge = re.findall(findJuge, item)[0]  # 评价人数
            data.append(juge)
            inq = re.findall(finInq, item)  # 概述
            if len(inq) != 0:
                inq = inq[0].replace('。', "")
                data.append(inq)
            else:
                data.append('')  # 留空
            bd = re.findall(finBd, item)[0]  #
            bd = re.sub(r'<br(\s+)?/>(\s+)?', " ", bd)
            data.append(bd.strip())
            date_list.append(data)
    return date_list


# 获取单个网页细腻些
def ask_url(url):
    head = {
        "User-Agent": "Mozilla / 5.0(Linux;Android 6.0;Nexus 5 Build/MRA58N) AppleWebKit / 537.36(KHTML, like"
                      "Gecko) Chrome / 87.0.4280.141 Mobile Safari/537.36"
    }
    request = urllib.request.Request(url=url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


# 3 保存数据
def save_date(datalist, path):
    print("save......")
    workbook = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    sheet = workbook.add_sheet("豆瓣电影top250")  # 创建工作表
    col = ("电影链接", "电影图片链接", "电影中文名", "电影英文名", "电影评分", "评价人数", "电影概述", "电影相关")
    for i in range(0, len(col)):
        sheet.write(0, i, col[i])
    for i in range(0, len(datalist)):
        print("写入第%d条" % (i + 1))
        data = datalist[i]
        for k in range(0, len(data)):
            sheet.write(i + 1, k, data[k])
    workbook.save(path)
    print('保存结束')


def save_data_to_db(db_path, data_lisst):
    init_db(db_path)
    conn = sqlite3.connect(db_path)
    cusor = conn.cursor()
    for data in data_lisst:
        for index in range(len(data)):
            if index == 4 or index == 5:
                continue
            else:
                data[index] = '"' + data[index] + '"'
        sql = '''
            insert into movie(link,pic_link,c_name,w_name,rate,juge,introduction,info)
            values(%s);
        ''' % ",".join(data)
        cusor.execute(sql)
    conn.commit()
    conn.close()
    print('存储完成')


def init_db(dbpath):
    conn = sqlite3.connect(dbpath)
    cusor = conn.cursor()
    sql = '''
        create table movie(
            id INTEGER primary key AUTOINCREMENT not null,
            link text,
            pic_link text,
            c_name varchar,
            w_name varchar,
            rate numeric,
            juge numeric,
            introduction text,
            info text
        );
    '''
    try:
        cusor.execute(sql)
    except sqlite3.OperationalError as e:
        if str(e) == "table movie already exists":
            print(e)

        else:
            raise e
    conn.commit()
    conn.close()
    print("数据库初始化完成")


if __name__ == '__main__':  # 执行spider.py时时吊桶函数

    main()

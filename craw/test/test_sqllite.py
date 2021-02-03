# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_sqllite
   Description :
   Author :       eddie
   date：          2021/1/21
-------------------------------------------------
   Change Activity:
                   2021/1/21:
-------------------------------------------------
"""
__author__ = 'eddie'

import sqlite3

connect = sqlite3.connect("test.db")
print("连接数据库")
c = connect.cursor()  # 获取游标
sql = '''
    create table sse
        (id int primary key not null,
        name text not null,
        age int not null,
        addresses text,
        salary real);
'''

sql1 = '''
        insert into sse(id,name,age,addresses,salary) 
                    values(1,'eddie',18,"重庆",8000)

'''

insert2 = '''
       insert into sse(id,name,age,addresses,salary)
                   values(2,'ben',27,"重庆",12000)
'''
deletesql = '''
        drop table student
'''
select = '''
        select * from sse;
'''
m = c.execute(select)  # 执行sql语句
for row in m:
    print(type(row))
# connect.commit()  # 提交sql
connect.close()  # 关闭连接
print("关闭连接")

# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_xwlt
   Description :
   Author :       eddie
   date：          2021/1/21
-------------------------------------------------
   Change Activity:
                   2021/1/21:
-------------------------------------------------
"""
__author__ = 'eddie'

import xlwt

# workbook
workbook = xlwt.Workbook(encoding='utf-8')
# 创建工作表
worksheet = workbook.add_sheet("sheet1")
for i in range(0, 9):
    for j in range(0, i + 1):
        worksheet.write(i, j, (str(j + 1) + "*" + str(i + 1) + "=" + str((i + 1) * (j + 1))))
# worksheet.write(0, 0, "dd")  # 第一个参数行，第二份参数列，第三个参数写入数据
workbook.save("students.xls")

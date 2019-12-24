# -*- coding: utf-8 -*-
'''
 @File    : common.py
 @Time    : 2019/12/24 10:49
 @Author  : Chenzd
 @Project : 公用方法
 @Software: PyCharm
'''
import os
import xlrd

# ---获取excel文件sheet页记录,返回的是列表数组---
def get_xls_case(xls_path,xls_name,sheet_name):
    cls = []
    xpath = os.path.join(xls_path, xls_name)
    file = xlrd.open_workbook(xpath)
    sheet = file.sheet_by_name(sheet_name)
    nrows = sheet.nrows
    for i in range(nrows):
        if sheet.row_values(i)[0] != u'test_modules':
            cls.append(sheet.row_values(i))
    return cls
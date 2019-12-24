# -*- coding: utf-8 -*-
'''
 @File    : filePath.py
 @Time    : 2019/12/21 15:49
 @Author  : Chenzd
 @Project :  文件路径管理
 @Software: PyCharm
'''

import os
import time

'''---一级目录---'''
pro_path = os.path.dirname(os.path.realpath(__file__))  # 获取当前文件目录，即当前项目目录
config_path = os.path.join(pro_path, 'config')  # 配置文件存放目录
result_path = os.path.join(pro_path,'result')  # 测试结果存放目录
testCase_path = os.path.join(pro_path,'testCase')  # 测试用例存放目录
testFile_path = os.path.join(pro_path,'testFile')  # 测试文件存放目录


'''---二级目录---'''
report_path = os.path.join(result_path, 'report')  # 测试报告存放目录
screenShot_path = os.path.join(result_path, 'screenShot')  # 运行屏幕截图存放目录
adbLog_path = os.path.join(result_path, 'adbLog')  # adb执行日志存放目录
log_path = os.path.join(result_path, 'log')  # adb执行日志存放目录

emailContent_filePath = os.path.join(testFile_path, 'emailcontent.html')  # 邮件模板文件

def get_filePath(file_path, file_type):
    day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
    filePath = os.path.join(file_path, day)
    if not os.path.exists(filePath):
        os.mkdir(filePath)
    fileName = os.path.join(filePath, now+file_type)
    return fileName

if __name__ == '__main__':
    print(get_filePath(log_path, '12.log'))

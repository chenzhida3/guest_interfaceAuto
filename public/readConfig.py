# -*- coding: utf-8 -*-
'''
 @File    : readConfig.py
 @Time    : 2019/12/21 16:09
 @Author  : Chenzd
 @Project : 读取配置文件
 @Software: PyCharm
'''

import configparser as cparser
import os
import filePath
from public.configLog import Logger

logger = Logger(logger='public.readConfig.ReadConfig').getlog()
config_file = os.path.join(filePath.config_path,'config.ini')

class ReadConfig:
    '''读取配置文件信息'''

    def __init__(self):
        self.configParser = cparser.ConfigParser()
        self.configParser.read(config_file)

    def get_mysql(self, name):
        value = self.configParser.get('mysql', name)
        logger.info('读取config.ini文件 mysql:[%s:%s]' % (name, value))
        return value

    def get_email(self,name):
        value = self.configParser.get('email',name)
        logger.info('读取config.ini文件 email:[%s:%s]' % (name, value))
        return value


if __name__ == '__main__':
    ReadConfig().get_mysql('host')
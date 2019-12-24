# -*- coding: utf-8 -*-
'''
 @File    : configDB.py
 @Time    : 2019/12/21 15:47
 @Author  : Chenzd
 @Project : 数据库操作配置
 @Software: PyCharm
'''
import time

import pymysql

from public.configLog import Logger
from public.readConfig import ReadConfig
readconfig = ReadConfig()
logger = Logger(logger='public.configDB.MysqlDB').getlog()
class MysqlDB:

    host = readconfig.get_mysql('host')
    port = readconfig.get_mysql('port')
    user = readconfig.get_mysql('user')
    password = readconfig.get_mysql('password')
    db_name = readconfig.get_mysql('db_name')
    config_dict = {
        'host': str(host),
        'port': int(port),
        'user': user,
        'password': password,
        'db': db_name,
        'charset': 'utf8mb4'
    }

    def __init__(self):
        self.db = None
        self.cursor = None

    '''连接数据库'''
    def connect_db(self):
        try:
            self.conn = pymysql.connect(**self.config_dict)
            self.cursor = self.conn.cursor()
            logger.info('连接数据库')
        except Exception as e:
            logger.error("mysql connect error %d : [%s]" % (e.args[0], e.args[1]))

    '''关闭连接'''
    def close_db(self):
        self.conn.close()

    '''删除数据'''
    def clear(self, table_name):
        # real_sql = "truncate table " + table_name + ";"
        real_sql = "delete from " + table_name + ";"
        print(real_sql)
        with self.cursor as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
        self.conn.commit()

    '''插入数据'''
    def insert(self, table_name, table_data):
        for key in table_data:
            table_data[key] = "'"+str(table_data[key])+"'"
        key = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ")"
        print(real_sql)
        with self.cursor as cusor:
            cusor.execute(real_sql)
        self.conn.commit()

    '''查询单条数据'''
    def selectOne(self, sql):
        self.cursor.execute(sql)
        res = self.cursor.fetchone()
        return res

    '''查询表内所有数据'''
    def selectAll(self, table_name):
        sql = 'select * from '+table_name
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        return res

    '''创建时间戳'''
    def createTime(self):
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


if __name__ == '__main__':
    db = MysqlDB()
    db.connect_db()
    table_name = 'sign_event'
    # data = {'id': 2, 'name': '小米', '`limit`': 100, 'status': 0,
    #         'address': '北京会展中心', 'start_time': '2019-12-30 23:59:59', 'create_time': MysqlDB().createTime()}
    # table_name2 = "sign_guest"
    # data2 = {'realname': 'alen', 'phone': 12312341234, 'email': 'alen@mail.com',
    #          'sign': 0, 'event_id': 1, 'create_time': '2016-08-20 00:25:42'}
    # db.insert(table_name, data)
    # db.clear(table_name)
    # db.close_db()
    # sql = "select * from sign_event where limit>%s" % str(100)
    print(db.selectAll(table_name))
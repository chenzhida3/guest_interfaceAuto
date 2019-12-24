# -*- coding: utf-8 -*-
'''
 @File    : add_dataDB.py
 @Time    : 2019/12/23 9:21
 @Author  : Chenzd
 @Project : 添加数据库测试数据
 @Software: PyCharm
'''
from public.configDB import MysqlDB
class test_data:

    # create data
    datas = {
        'sign_event': [
            {'id': 1, 'name': '红米Pro 发布会', '`limit`': 2000, 'status': 1,
             'address': '北京会展中心', 'start_time': '2020-08-20 14:00:00', 'create_time': MysqlDB().createTime()},
            {'id': 2, 'name': '华为P系列发布会', '`limit`': 0, 'status': 1,
             'address': '北京会展中心', 'start_time': '2017-08-20 14:00:00', 'create_time': MysqlDB().createTime()},
            {'id': 3, 'name': '华为mata系列发布会', '`limit`': 2000, 'status': 0,
             'address': '北京会展中心', 'start_time': '2016-08-20 14:00:00', 'create_time': MysqlDB().createTime()},
            {'id': 4, 'name': '红米Pro 发布会', '`limit`': 2000, 'status': 1,
             'address': '北京会展中心', 'start_time': '2010-08-20 14:00:00', 'create_time': MysqlDB().createTime()},
            {'id': 5, 'name': '华晨宇演唱会', '`limit`': 2000, 'status': 1,
             'address': '北京国家会议中心', 'start_time': '2020-08-20 14:00:00', 'create_time': MysqlDB().createTime()},
        ],
        'sign_guest': [
            {'id': 1, 'realname': 'alen', 'phone': 18600000120, 'email': 'alen@mail.com',
             'sign': 0, 'event_id': 1, 'create_time': MysqlDB().createTime()},
            {'id': 2, 'realname': 'kangkang', 'phone': 18600000121, 'email': 'kangkang@mail.com',
             'sign': 1, 'event_id': 2, 'create_time': MysqlDB().createTime()},
            {'id': 3, 'realname': 'tom', 'phone': 18600000122, 'email': 'tom@mail.com',
             'sign': 0, 'event_id': 5, 'create_time': MysqlDB().createTime()},
            {'id': 4, 'realname': 'appium', 'phone': 18600000123, 'email': 'appium@mail.com',
             'sign': 1, 'event_id': 1, 'create_time': MysqlDB().createTime()},
            {'id': 5, 'realname': 'czd', 'phone': 15606920337, 'email': 'czd@mail.com',
             'sign': 0, 'event_id': 5, 'create_time': MysqlDB().createTime()},
            {'id': 6, 'realname': 'czc', 'phone': 15606920336, 'email': 'czc@mail.com',
             'sign': 0, 'event_id': 4, 'create_time': MysqlDB().createTime()},
        ],
    }

    def init_data(self):
        db = MysqlDB()
        for table, data in self.datas.items():
            db.connect_db()
            db.clear(table)
            for d in data:
                db.connect_db()
                db.insert(table, d)
        db.close_db()


if __name__ == '__main__':
    test_data().init_data()
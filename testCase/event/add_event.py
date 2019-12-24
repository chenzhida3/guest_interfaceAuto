# -*- coding: utf-8 -*-
'''
 @File    : add_event.py
 @Time    : 2019/12/23 10:08
 @Author  : Chenzd
 @Project : 添加发布会测试
 @Software: PyCharm
'''
import unittest
from public.configDB import MysqlDB
import requests
from testData.add_dataDB import test_data
from public.configLog import Logger
logger = Logger(logger='testCase.event.add_event.Add_event').getlog()

class Add_event(unittest.TestCase):
    '''添加发布会'''

    @classmethod
    def setUpClass(cls):
        test_data().init_data()
        cls.base_url = "http://127.0.0.1:8000/api/add_event/"

    def tearDown(self):
        print(self.result)

    def test01_paramsNull(self):
        '''参数为空'''
        logger.info('=============添加发布会接口--参数为空================')
        payload = {'eid': '', 'name': '', 'limit': '', 'address': "", 'start_time': '', 'create_time': ''}
        res = requests.post(self.base_url, data=payload)
        self.result = res.json()
        self.assertEqual(10021, self.result['status'], '结果：返回的状态码不对')
        self.assertEqual('parameter error', self.result['message'], '结果：返回的提示语不对')

    def test02_idExit(self):
        '''发布会id已存在'''
        logger.info('==========添加发布会接口--发布会id已存在==============')
        payload = {'eid': 1, 'name': '平和蜜柚节', 'limit': '5000', 'address': "漳州平和",
                   'start_time': '2020-10-15 18:00:00', 'create_time': MysqlDB().createTime()}
        res = requests.post(self.base_url, data=payload)
        self.result = res.json()
        self.assertEqual(10022, self.result['status'], '结果：返回的状态码不对')
        self.assertEqual('event id already exits', self.result['message'], '结果：返回的提示语不对')

    def test03_nameExit(self):
        '''发布会名称已存在'''
        logger.info('==========添加发布会接口--发布会名称已存在==============')
        payload = {'eid': 7, 'name': '华晨宇演唱会', 'limit': '200', 'address': "厦门体育馆",
                   'start_time': '2018-10-15 18:00:00', 'create_time': MysqlDB().createTime()}
        res = requests.post(self.base_url, data=payload)
        self.result = res.json()
        self.assertEqual(10023, self.result['status'], '结果：返回的状态码不对')
        self.assertEqual('event name already exits', self.result['message'], '结果：返回的提示语不对')

    def test04_timeFormat(self):
        '''时间格式错误'''
        logger.info('==========添加发布会接口--时间格式错误==============')
        payload = {'eid': 6, 'name': '林俊杰演唱会', 'limit': '200', 'address': "厦门体育馆",
                   'start_time': '2018-10-15_18:00:00', 'create_time': MysqlDB().createTime()}
        res = requests.post(self.base_url, data=payload)
        self.result = res.json()
        self.assertEqual(10024, self.result['status'], '结果：返回的状态码不对')
        self.assertEqual('start_time format error.It must be in YYYY-MM-DD HH:MM:SS format.',
                         self.result['message'], '结果：返回的提示语不对')

    def test05_success(self):
        '''添加成功'''
        logger.info('============添加发布会接口--添加成功===============')
        payload = {'eid': 6, 'name': '林俊杰演唱会', 'limit': '200', 'address': "厦门体育馆",
                   'start_time': '2020-10-15 18:00:00', 'create_time': MysqlDB().createTime()}
        res = requests.post(self.base_url, data=payload)
        self.result = res.json()
        self.assertEqual(200, self.result['status'], '结果：返回的状态码不对')
        self.assertEqual('add event success', self.result['message'], '结果：返回的提示语不对')


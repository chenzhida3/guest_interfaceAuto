# -*- coding: utf-8 -*-
'''
 @File    : get_event.py
 @Time    : 2019/12/23 14:45
 @Author  : Chenzd
 @Project : 发布会查询接口---增加用户认证
 @Software: PyCharm
'''
import unittest
import requests
from testData.add_dataDB import test_data
from public.configLog import Logger
logger = Logger(logger='testCase.event.get_event_sec.Get_event_sec').getlog()

class Get_event_sec(unittest.TestCase):
    '''查询发布会--增加用户认证'''

    @classmethod
    def setUpClass(cls):
        cls.base_url = "http://127.0.0.1:8000/api/sec_get_event_list/"
        cls.auth_user = ('chenzd', 'czd158805')

    def tearDown(self):
        print(self.result)

    def test01_authNull(self):
        '''auth参数为空'''
        logger.info('=============查询发布会接口--auth参数为空================')
        payload = {'eid': ''}
        res = requests.get(self.base_url, params=payload)
        self.result = res.json()
        self.assertEqual(10011, self.result['status'], '结果：返回的状态码不对')
        self.assertEqual('user auth null', self.result['message'], '结果：返回的提示语不对')

    def test02_authErr(self):
        '''auth参数为错误'''
        logger.info('=============查询发布会接口--auth参数为错误================')
        payload = {'eid': '1'}
        res = requests.get(self.base_url, params=payload, auth=('abc', '123'))
        self.result = res.json()
        self.assertEqual(10012, self.result['status'], '结果：返回的状态码不对')
        self.assertEqual('user auth fail', self.result['message'], '结果：返回的提示语不对')

    def test03_paramsNull(self):
        '''参数为空'''
        logger.info('=============查询发布会接口--参数为空================')
        payload = {'eid': ''}
        res = requests.get(self.base_url, params=payload, auth=self.auth_user)
        self.result = res.json()
        self.assertEqual(10021, self.result['status'], '结果：返回的状态码不对')
        self.assertEqual('parameter error', self.result['message'], '结果：返回的提示语不对')

    def test04_eventNull_id(self):
        '''发布会查询结果为空'''
        logger.info('==========查询发布会接口--发布会查询结果为空==============')
        payload = {'eid': 10}
        res = requests.get(self.base_url, params=payload, auth=self.auth_user)
        self.result = res.json()
        self.assertEqual(10022, self.result['status'], '结果：返回的状态码不对')
        self.assertEqual('query result is empty', self.result['message'], '结果：返回的提示语不对')

    def test05_eventNull_name(self):
        '''发布会查询结果为空'''
        logger.info('==========查询发布会接口--发布会查询结果为空==============')
        payload = {'name': '陈大帅哥'}
        res = requests.get(self.base_url, params=payload, auth=self.auth_user)
        self.result = res.json()
        self.assertEqual(10022, self.result['status'], '结果：返回的状态码不对')
        self.assertEqual('query result is empty', self.result['message'], '结果：返回的提示语不对')

    def test06_success_id(self):
        '''发布会查询成功'''
        logger.info('==========查询发布会接口--发布会查询成功==============')
        payload = {'eid': 1}
        res = requests.get(self.base_url, params=payload, auth=self.auth_user)
        self.result = res.json()
        self.assertEqual(200, self.result['status'], '结果：返回的状态码不对')
        self.assertEqual('success', self.result['message'], '结果：返回的提示语不对')

    def test07_success_name(self):
        '''发布会查询成功'''
        logger.info('============查询发布会接口--发布会查询成功===============')
        payload = {'name': '红米Pro 发布会'}
        res = requests.get(self.base_url, params=payload, auth=self.auth_user)
        self.result = res.json()
        self.assertEqual(200, self.result['status'], '结果：返回的状态码不对')
        self.assertEqual('success', self.result['message'], '结果：返回的提示语不对')
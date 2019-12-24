# -*- coding: utf-8 -*-
'''
 @File    : get_guest.py
 @Time    : 2019/12/23 15:13
 @Author  : Chenzd
 @Project : 查询嘉宾接口
 @Software: PyCharm
'''
import unittest
import requests
from testData.add_dataDB import test_data
from public.configLog import Logger
logger = Logger(logger='testCase.guest.get_guest.Get_guest').getlog()

class Get_guest(unittest.TestCase):
    '''查询嘉宾'''

    @classmethod
    def setUpClass(cls):
        # test_data().init_data()
        cls.base_url = "http://127.0.0.1:8000/api/get_guest_list/"

    def tearDown(self):
        print(self.result)

    def test01_paramsNull(self):
        '''参数为空'''
        logger.info('=============查询嘉宾接口--参数为空================')
        payload = {'eid': ''}
        res = requests.get(self.base_url, params=payload)
        self.result = res.json()
        self.assertEqual(10021, self.result['status'], '结果：返回的状态码不对')
        self.assertEqual('eid cannot be empty', self.result['message'], '结果：返回的提示语不对')

    def test02_success_id(self):
        '''嘉宾查询成功'''
        logger.info('==========查询嘉宾接口--嘉宾查询成功==============')
        payload = {'eid': 1, 'phone': ''}
        res = requests.get(self.base_url, params=payload)
        self.result = res.json()
        self.assertEqual(200, self.result['status'], '结果：返回的状态码不对')
        self.assertEqual('success', self.result['message'], '结果：返回的提示语不对')

    def test03_guestNull_id(self):
        '''嘉宾查询结果为空'''
        logger.info('==========查询嘉宾接口--嘉宾查询结果为空==============')
        payload = {'eid': 3, 'phone': ''}
        res = requests.get(self.base_url, params=payload)
        self.result = res.json()
        self.assertEqual(10022, self.result['status'], '结果：返回的状态码不对')
        self.assertEqual('request result is empty', self.result['message'], '结果：返回的提示语不对')

    def test04_guestNull(self):
        '''嘉宾查询结果为空'''
        logger.info('==========查询嘉宾接口--嘉宾查询结果为空==============')
        payload = {'eid': 3, 'phone': 12345678910}
        res = requests.get(self.base_url, params=payload)
        self.result = res.json()
        self.assertEqual(10022, self.result['status'], '结果：返回的状态码不对')
        self.assertEqual('request result is empty', self.result['message'], '结果：返回的提示语不对')

    def test05_success(self):
        '''嘉宾查询成功'''
        logger.info('============查询嘉宾接口--嘉宾查询成功===============')
        payload = {'eid': 1, 'phone': '18600000123'}
        res = requests.get(self.base_url, params=payload)
        self.result = res.json()
        self.assertEqual(200, self.result['status'], '结果：返回的状态码不对')
        self.assertEqual('success', self.result['message'], '结果：返回的提示语不对')
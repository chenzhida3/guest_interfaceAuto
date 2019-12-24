# -*- coding: utf-8 -*-
'''
 @File    : sign_guest.py
 @Time    : 2019/12/23 15:24
 @Author  : Chenzd
 @Project : 用户签到接口
 @Software: PyCharm
'''
import unittest
import requests
from testData.add_dataDB import test_data
from  public.configLog import Logger
logger = Logger(logger='testCase.guest.sign_guest.Sign_guest').getlog()
class Sign_guest(unittest.TestCase):
    '''用户签到接口'''

    @classmethod
    def setUpClass(cls):
        # test_data().init_data()
        cls.baseUrl = "http://127.0.0.1:8000/api/user_sign/"

    def tearDown(self):
        print(self.result)

    def test01_paramErr(self):
        '''参数错误'''
        logger.info('===============用户签到接口----参数错误=================')
        payload = {'eid': '', 'phone': ''}
        res = requests.post(self.baseUrl, data=payload)
        self.result = res.json()
        self.assertEqual(10021, self.result['status'])
        self.assertEqual('parameter error', self.result['message'])

    def test02_idNull(self):
        '''发布会id为查询结果为空'''
        logger.info('===============用户签到接口----发布会id为查询结果为空=================')
        payload = {'eid': 10, 'phone': '15606920337'}
        res = requests.post(self.baseUrl, data=payload)
        self.result = res.json()
        self.assertEqual(10022, self.result['status'])
        self.assertEqual('event id is null', self.result['message'])

    def test03_statusClose(self):
        '''发布会状态已关闭'''
        logger.info('===============用户签到接口----发布会状态已关闭=================')
        payload = {'eid': 3, 'phone': '15606920337'}
        res = requests.post(self.baseUrl, data=payload)
        self.result = res.json()
        self.assertEqual(10023, self.result['status'])
        self.assertEqual('event status is not available', self.result['message'])

    def test04_eventStart(self):
        '''发布会已经开始'''
        logger.info('===============用户签到接口----发布会已经开始=================')
        payload = {'eid': 4, 'phone': '15606920336'}
        res = requests.post(self.baseUrl, data=payload)
        self.result = res.json()
        self.assertEqual(10024, self.result['status'])
        self.assertEqual('event has started', self.result['message'])

    def test05_phoneNull(self):
        '''嘉宾手机号码查询不到'''
        logger.info('===============用户签到接口----嘉宾手机号码查询不到=================')
        payload = {'eid': 1, 'phone': 16545102121}
        res = requests.post(self.baseUrl, data=payload)
        self.result = res.json()
        self.assertEqual(10025, self.result['status'])
        self.assertEqual('user phone is null', self.result['message'])

    def test06_userNot(self):
        '''用户未参加会议'''
        logger.info('===============用户签到接口----用户未参加会议=================')
        payload = {'eid': 1, 'phone': 18600000121}
        res = requests.post(self.baseUrl, data=payload)
        self.result = res.json()
        self.assertEqual(10026, self.result['status'])
        self.assertEqual('user did not participate in the conference', self.result['message'])

    def test07_signExit(self):
        '''用户已签到'''
        logger.info('===============用户签到接口----用户已签到=================')
        payload = {'eid': 1, 'phone': 18600000123}
        res = requests.post(self.baseUrl, data=payload)
        self.result = res.json()
        self.assertEqual(10027, self.result['status'])
        self.assertEqual('user already sign', self.result['message'])

    def test07_signSuccess(self):
        '''签到成功'''
        logger.info('===============用户签到接口----签到成功=================')
        payload = {'eid': 5, 'phone': '15606920337'}
        res = requests.post(self.baseUrl, data=payload)
        self.result = res.json()
        self.assertEqual(200, self.result['status'])
        self.assertEqual('sign success', self.result['message'])
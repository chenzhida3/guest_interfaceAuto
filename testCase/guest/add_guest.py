# -*- coding: utf-8 -*-
'''
 @File    : add_guest.py
 @Time    : 2019/12/23 13:47
 @Author  : Chenzd
 @Project : 添加嘉宾接口
 @Software: PyCharm
'''
import unittest
import requests
from testData.add_dataDB import test_data
from public.configDB import MysqlDB
from  public.configLog import Logger
logger = Logger(logger='testCase.guest.add_guest.Add_guest').getlog()
class Add_guest(unittest.TestCase):
    '''添加嘉宾'''

    @classmethod
    def setUpClass(cls):
        # test_data().init_data()
        cls.baseUrl = "http://127.0.0.1:8000/api/add_guest/"

    def tearDown(self):
        print(self.result)

    def test01_paramErr(self):
        '''参数错误'''
        logger.info('===============添加嘉宾接口----参数错误=================')
        payload = {'eid': 1, 'reaname': 'czd', 'phone': '15606920337', 'email': 'czd@mail.com',
                   'create_time': MysqlDB().createTime()}
        res = requests.post(self.baseUrl, data=payload)
        self.result = res.json()
        self.assertEqual(10021, self.result['status'])
        self.assertEqual('parameter error', self.result['message'])

    def test02_idNull(self):
        '''发布会id为空'''
        logger.info('===============添加嘉宾接口----发布会id为空=================')
        payload = {'eid': 10, 'realname': 'czd', 'phone': '15606920337', 'email': 'czd@mail.com',
                   'create_time': MysqlDB().createTime()}
        res = requests.post(self.baseUrl, data=payload)
        self.result = res.json()
        self.assertEqual(10022, self.result['status'])
        self.assertEqual('event id null', self.result['message'])

    def test03_statusClose(self):
        '''发布会状态已关闭'''
        logger.info('===============添加嘉宾接口----发布会状态已关闭=================')
        payload = {'eid': 3, 'realname': 'czd', 'phone': '15606920337', 'email': 'czd@mail.com',
                   'create_time': MysqlDB().createTime()}
        res = requests.post(self.baseUrl, data=payload)
        self.result = res.json()
        self.assertEqual(10023, self.result['status'])
        self.assertEqual('event status is not available', self.result['message'])

    def test04_full(self):
        '''发布会人数已满'''
        logger.info('===============添加嘉宾接口----发布会人数已满=================')
        payload = {'eid': 2, 'realname': 'czd', 'phone': '15606920337', 'email': 'czd@mail.com',
                   'create_time': MysqlDB().createTime()}
        res = requests.post(self.baseUrl, data=payload)
        self.result = res.json()
        self.assertEqual(10024, self.result['status'])
        self.assertEqual('event number is full', self.result['message'])

    def test05_eventStart(self):
        '''发布会已经开始'''
        logger.info('===============添加嘉宾接口----发布会已经开始=================')
        payload = {'eid': 4, 'realname': 'czd', 'phone': '15606920337', 'email': 'czd@mail.com',
                   'create_time': MysqlDB().createTime()}
        res = requests.post(self.baseUrl, data=payload)
        self.result = res.json()
        self.assertEqual(10025, self.result['status'])
        self.assertEqual('event has started', self.result['message'])

    def test06_phoneRepeat(self):
        '''嘉宾手机号码重复'''
        logger.info('===============添加嘉宾接口----嘉宾手机号码重复=================')
        payload = {'eid': 1, 'realname': 'czd', 'phone': '18600000120', 'email': 'czd@mail.com',
                   'create_time': MysqlDB().createTime()}
        res = requests.post(self.baseUrl, data=payload)
        self.result = res.json()
        self.assertEqual(10026, self.result['status'])
        self.assertEqual('the event guest phone number repeat', self.result['message'])

    def test07_phoneFomat(self):
        '''嘉宾手机号码格式错误'''
        logger.info('===============添加嘉宾接口----嘉宾手机号码重复=================')
        payload = {'eid': 1, 'realname': 'czd', 'phone': '1560692033', 'email': 'czd@mail.com',
                   'create_time': MysqlDB().createTime()}
        res = requests.post(self.baseUrl, data=payload)
        self.result = res.json()
        self.assertEqual(10027, self.result['status'])
        self.assertEqual('phone format error', self.result['message'])

    def test08_success(self):
        '''添加嘉宾成功'''
        logger.info('===============添加嘉宾接口----添加嘉宾成功=================')
        payload = {'eid': 1, 'realname': 'czd', 'phone': '15606920337', 'email': 'czd@mail.com',
                   'create_time': MysqlDB().createTime()}
        res = requests.post(self.baseUrl, data=payload)
        self.result = res.json()
        self.assertEqual(200, self.result['status'])
        self.assertEqual('add guest success', self.result['message'])
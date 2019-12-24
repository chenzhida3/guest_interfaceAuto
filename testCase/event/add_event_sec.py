# -*- coding: utf-8 -*-
'''
 @File    : add_event_sec.py
 @Time    : 2019/12/23 10:08
 @Author  : Chenzd
 @Project : 添加发布会---MD5加密
 @Software: PyCharm
'''
import hashlib
import time
import unittest
from public.configDB import MysqlDB
import requests
from testData.add_dataDB import test_data
from public.configLog import Logger
logger = Logger(logger='testCase.event.add_event_sec.Add_event_sec').getlog()

class Add_event_sec(unittest.TestCase):
    '''添加发布会--md5加密验证'''
    # test_data().init_data()
    def setUp(self):
        self.base_url = "http://127.0.0.1:8000/api/sec_add_event/"
        self.api_key = '&Guest-Bugmaster'
        self.now_time = time.time()
        self.client_time = str(self.now_time).split('.')[0]
        md5 = hashlib.md5()
        sign_str = self.client_time + self.api_key
        sign_str_utf8 = sign_str.encode(encoding='utf-8')
        md5.update(sign_str_utf8)
        self.sign_md5 = md5.hexdigest()

    def tearDown(self):
        print(self.result)

    def test01_signNull(self):
        '''签名为空'''
        logger.info('=============添加发布会接口--签名为空================')
        payload = {'eid': '1', 'name': '', 'limit': '', 'address': "", 'start_time': '', 'create_time': '',
                   'time': '', 'sign': ''}
        res = requests.post(self.base_url, data=payload)
        self.result = res.json()
        self.assertEqual(10011, self.result['status'], '结果：返回的状态码不对')
        self.assertEqual('user sign null', self.result['message'], '结果：返回的提示语不对')

    def test02_signTimeOut(self):
        '''签名超时'''
        logger.info('=============添加发布会接口--签名超时================')
        now_time = str(int(self.client_time) - 61)
        payload = {'eid': '1', 'name': '', 'limit': '', 'address': "", 'start_time': '', 'create_time': '',
                   'time': now_time, 'sign': 'abc'}
        res = requests.post(self.base_url, data=payload)
        self.result = res.json()
        self.assertEqual(10012, self.result['status'], '结果：返回的状态码不对')
        self.assertEqual('user sign timeout', self.result['message'], '结果：返回的提示语不对')

    def test03_signErr(self):
        '''签名错误'''
        logger.info('=============添加发布会接口--签名错误================')
        payload = {'eid': '1', 'name': '', 'limit': '', 'address': "", 'start_time': '', 'create_time': '',
                   'time': self.client_time, 'sign': '123'}
        res = requests.post(self.base_url, data=payload)
        self.result = res.json()
        self.assertEqual(10013, self.result['status'], '结果：返回的状态码不对')
        self.assertEqual('user sign error', self.result['message'], '结果：返回的提示语不对')

    def test04_paramsNull(self):
        '''参数为空'''
        logger.info('=============添加发布会接口--参数为空================')
        payload = {'eid': '1', 'name': '', 'limit': '', 'address': "", 'start_time': '', 'create_time': '',
                   'time': self.client_time, 'sign': self.sign_md5}
        res = requests.post(self.base_url, data=payload)
        self.result = res.json()
        self.assertEqual(10021, self.result['status'], '结果：返回的状态码不对')
        self.assertEqual('parameter error', self.result['message'], '结果：返回的提示语不对')

    def test05_idExit(self):
        '''发布会id已存在'''
        logger.info('==========添加发布会接口--发布会id已存在==============')
        payload = {'eid': 1, 'name': '平和蜜柚节', 'limit': '5000', 'address': "漳州平和",
                   'start_time': '2020-10-15 18:00:00', 'create_time': MysqlDB().createTime(),
                   'time': self.client_time, 'sign': self.sign_md5}
        res = requests.post(self.base_url, data=payload)
        self.result = res.json()
        self.assertEqual(10022, self.result['status'], '结果：返回的状态码不对')
        self.assertEqual('event id already exits', self.result['message'], '结果：返回的提示语不对')

    def test06_nameExit(self):
        '''发布会名称已存在'''
        logger.info('==========添加发布会接口--发布会名称已存在==============')
        payload = {'eid': 7, 'name': '华晨宇演唱会', 'limit': '200', 'address': "厦门体育馆",
                   'start_time': '2018-10-15 18:00:00', 'create_time': MysqlDB().createTime(),
                   'time': self.client_time, 'sign': self.sign_md5}
        res = requests.post(self.base_url, data=payload)
        self.result = res.json()
        self.assertEqual(10023, self.result['status'], '结果：返回的状态码不对')
        self.assertEqual('event name already exits', self.result['message'], '结果：返回的提示语不对')

    def test07_timeFormat(self):
        '''时间格式错误'''
        logger.info('==========添加发布会接口--时间格式错误==============')
        payload = {'eid': 8, 'name': '罗志祥演唱会', 'limit': '200', 'address': "厦门体育馆",
                   'start_time': '2018-10-15_18:00:00', 'create_time': MysqlDB().createTime(),
                   'time': self.client_time, 'sign': self.sign_md5}
        res = requests.post(self.base_url, data=payload)
        self.result = res.json()
        self.assertEqual(10024, self.result['status'], '结果：返回的状态码不对')
        self.assertEqual('start_time format error.It must be in YYYY-MM-DD HH:MM:SS format.',
                         self.result['message'], '结果：返回的提示语不对')

    def test08_success(self):
        '''添加成功'''
        logger.info('============添加发布会接口--添加成功===============')
        payload = {'eid': 9, 'name': 'JJ演唱会', 'limit': '200', 'address': "厦门体育馆",
                   'start_time': '2020-10-15 18:00:00', 'create_time': MysqlDB().createTime(),
                   'time': self.client_time, 'sign': self.sign_md5}
        res = requests.post(self.base_url, data=payload)
        self.result = res.json()
        self.assertEqual(200, self.result['status'], '结果：返回的状态码不对')
        self.assertEqual('add event success', self.result['message'], '结果：返回的提示语不对')


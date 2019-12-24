# -*- coding: utf-8 -*-
'''
 @File    : runmain.py
 @Time    : 2019/12/21 15:29
 @Author  : Chenzd
 @Project : 主程序调用入口
 @Software: PyCharm
'''
import unittest
from public import common
from public.configEmail import Email
from public.configLog import Logger
from public.readConfig import ReadConfig
from runner import HTMLTestRunner
import filePath


logger = Logger(logger='runMain.RunMain').getlog()
caseList_xls = common.get_xls_case(filePath.testFile_path, 'caseList.xlsx', 'interface_testCase')
config = ReadConfig()
testCase = []

class RunMain():
    def __init__(self):
        self.caseFile = filePath.testCase_path  # 用例目录
        # self.reportPath = file_path.report_path  #报告存放路径
        self.mail = Email()   # 定义send mail 对象，最后根据配置文件判断是否发送
        self.isSend = config.get_email('isSend')
        self.caseList = []

    def set_case_list(self):
        for i, val in enumerate(caseList_xls):
            if int(val[3]) == 0:
                self.caseList.append(val[2])
        print(self.caseList)


    def set_case_suite(self):
        self.set_case_list()
        test_suite = unittest.TestSuite()
        suite_module = []

        for case in self.caseList:
            case_name = case.split("/")[-1]
            print(case_name + ".py")
            discover = unittest.defaultTestLoader.discover(self.caseFile, pattern=case_name + '.py', top_level_dir=None)
            suite_module.append(discover)

        if len(suite_module) > 0:

            for suite in suite_module:
                for test_name in suite:
                    test_suite.addTest(test_name)
        else:
            return None

        return test_suite

    def run(self):
        filename = filePath.get_filePath(filePath.report_path, '_result.html')
        fp = open(filename, 'wb')
        try:
            suit = self.set_case_suite()
            if suit is not None:
                logger.info("-----------test start------------")
                runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'发布会签到系统接口自动化测试报告', description=u'用例执行情况如下：')
                runner.run(suit)
            else:
                logger.info(" no case to test.")
        except Exception as ex:
            logger.error(str(ex))
        finally:
            logger.info("-----------test end------------")
            fp.close()
            # send test report by email
            if self.isSend == 'on':
                self.mail.send_mail(filename)
            elif self.isSend == 'off':
                logger.info("doesn't send result email to .")
            else:
                logger.info("unknow state.")
if __name__=='__main__':
    RunMain().run()
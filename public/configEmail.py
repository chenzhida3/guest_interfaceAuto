# -*- coding: utf-8 -*-
'''
 @File    : configEmail.py
 @Time    : 2019/12/24 10:51
 @Author  : Chenzd
 @Project : 邮件配置
 @Software: PyCharm
'''
import os
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import filePath
from public.readConfig import ReadConfig

readConfig = ReadConfig()

class Email():
    def __init__(self):
        global host_ip,host_port,mail_user,mail_passwd,send_user
        host_ip = readConfig.get_email("host")
        host_port = readConfig.get_email("port")
        mail_user = readConfig.get_email("mail_user")
        mail_passwd = readConfig.get_email("mail_passwd")
        send_user = readConfig.get_email("send_user")
        # get receiver list
        self.receiver = readConfig.get_email("rec_users")
        self.rec_users = []
        for i in str(self.receiver).split(","):
            self.rec_users.append(i)
        # defined email subject
        self.subject = "发布会签到系统接口自动化测试报告" + " " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        self.msg = MIMEMultipart('related')

    def config_header(self):
        self.msg['subject'] = self.subject
        self.msg['from'] = send_user
        self.msg['to'] = ";".join(self.rec_users)  # 接收邮件方

    def config_content(self):
        f = open(filePath.emailContent_filePath, 'r', encoding='UTF-8')
        content = f.read()
        f.close()
        content_plain = MIMEText(content, 'html', 'UTF-8')
        self.msg.attach(content_plain)

    def config_file(self,reportfile):
        # 添加附件
        reportfile_name=os.path.basename(reportfile)
        att = MIMEText(open(reportfile, "rb").read(), 'base64', 'utf-8')
        att['Content-Type'] = 'application/octet-stream'
        att['Content-Disposition'] = 'attachment; filename='+reportfile_name+''
        self.msg.attach(att)

    def send_mail(self,reportfile):
        self.config_header()
        self.config_content()
        self.config_file(reportfile)
        try:
            smtp = smtplib.SMTP_SSL(host_ip, host_port)
        except:
            smtp = smtplib.SMTP()
            smtp.connect(host_ip, host_port)
        # 用户名密码
        smtp.login(mail_user, mail_passwd)
        smtp.sendmail(send_user, self.rec_users, self.msg.as_string())
        smtp.quit()
if __name__ == '__main__':
    mail =Email()
    mail.send_mail()
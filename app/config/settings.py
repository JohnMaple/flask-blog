# -*- coding: utf-8 -*-
"""
    @description: 公共配置
"""
import os

__author__ = 'Henry'


# token 过期时间
TOKEN_EXPIRATION = eval(str(os.getenv('TOKEN_EXPIRATION'))) or 7200

# 邮件
MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.163.com')
MAIL_PORT = int(os.getenv('MAIL_PORT', 465))
MAIL_USE_SSL = True if 'true' == os.getenv('MAIL_USE_SSL') else False
MAIL_USE_TSL = True if 'true' == os.getenv('MAIL_USE_TSL') else False
MAIL_USERNAME = os.getenv('MAIL_USERNAME', '')
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', '')
MAIL_SUBJECT_PREFIX = os.getenv('MAIL_SUBJECT_PREFIX', '[timhub]')
MAIL_SENDER = os.getenv('MAIL_SENDER', 'timhub <timhub@163.com>')

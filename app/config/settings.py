# -*- coding: utf-8 -*-
"""
    @description: 公共配置
"""
import os

__author__ = 'Henry'


# token 过期时间
TOKEN_EXPIRATION = eval(str(os.getenv('TOKEN_EXPIRATION'))) or 7200



# -*- coding: utf-8 -*-
"""
    @description:
"""
from enum import Enum

__author__ = 'Henry'


class ClientTypeEnum(Enum):
    USER_NAME = 100
    USER_EMAIL = 101
    USER_MOBILE = 102

    # 微信小程序
    USER_MINA = 200

    # 微信公众号
    USER_WX = 201

    USER_QQ = 300
    USER_WEIBO = 400
    USER_GITHUB = 500


class StatusEnum(Enum):
    DELETE = 0  # 删除
    NORMAL = 1  # 正常
    HIDDEN = 2  # 隐藏



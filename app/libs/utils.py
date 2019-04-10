# -*- coding: utf-8 -*-
"""
    @description: 工具函数
"""
import random
from flask import jsonify
from app.libs.code import Code
from app.libs.error_code import Success

__author__ = 'Henry'


def make_result(msg=None, data=None, error_code=0, extend=None):
    """统一返回接口和异常返回接口一样"""
    # msg = msg if msg else (Code.msg[error_code] if Code.msg[error_code] else '')
    #
    # res = dict(
    #     error_code=error_code,
    #     msg=msg,
    #     data=data
    # )
    #
    # # 判断extend是否是一个字典，res中的key会被extend覆盖
    # if extend and isinstance(extend, dict):
    #     res.update(extend)
    #
    # return jsonify(res)

    return Success(msg=msg, error_code=error_code, data=data, extend=extend)


def create_nonce_str(n):
    # 获取nonceStr（随机字符串）
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    nonce_str = ""
    for i in range(0, n):
        s = random.randint(0, len(chars)-1)
        nonce_str += chars[s:s+1]
    return nonce_str


def get_captcha(length=4):
    """生成验证码"""
    code = ""
    for i in range(length):
        code += str(random.randint(0, 9))
    return code



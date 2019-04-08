# -*- coding: utf-8 -*-
"""
    @description: 工具函数
"""
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


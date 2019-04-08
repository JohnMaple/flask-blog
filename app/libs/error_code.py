# -*- coding: utf-8 -*-
"""
    @description: 自定义错误异常处理
"""
from app.libs.error import APIException

__author__ = 'Henry'


class Success(APIException):
    code = 200
    msg = 'ok'
    error_code = 0


class UpdateSuccess(Success):
    code = 201
    error_code = 1


class DeleteSuccess(Success):
    code = 202
    error_code = 2


class ServerError(APIException):
    code = 500
    msg = 'sorry, we made a mistake (*￣︶￣)!'
    error_code = 999


class ClientTypeError(APIException):
    # restful 状态码
    # 400 请求参数错误
    # 401 未授权
    # 403 禁止访问
    # 404 未找到页面
    # 500 服务器产生未知错误
    # 200 请求成功
    # 201 创建或更新成功
    # 204 删除成功
    # 301 302 重定向 302重定向只是暂时的重定向，搜索引擎会抓取新的内容而保留旧的地址，因为服务器返回302，所以，搜索搜索引擎认为新的网址是暂时的。
    # 而301重定向是永久的重定向，搜索引擎在抓取新的内容的同时也将旧的网址替换为了重定向之后的网址

    # code = 400
    # description = (
    #     'client is invalid'
    # )

    code = 400
    msg = 'client is invalid'
    error_code = 1006


class ParameterException(APIException):
    code = 400
    msg = 'invalid parameters'
    error_code = 1000


class NotFound(APIException):
    code = 404
    msg = 'the resource are not found O__O...'
    error_code = 1001


class AuthFailed(APIException):
    code = 401
    msg = 'authorization failed'
    error_code = 1005


class Forbidden(APIException):
    code = 403
    msg = 'forbidden, not in scope'
    error_code = 1004




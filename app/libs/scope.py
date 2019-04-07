# -*- coding: utf-8 -*-
"""
    @description:
"""

__author__ = 'Henry'


class Scope:
    """
        权限基类
    """
    allow_api = []
    allow_module = []
    forbidden = []

    def __add__(self, other):
        # 运算符重载
        self.allow_api = self.allow_api + other.allow_api
        # 去重
        self.allow_api = list(set(self.allow_api))

        # 运算符重载
        self.allow_module = self.allow_module + other.allow_module
        # 去重
        self.allow_module = list(set(self.allow_module))

        # 运算符重载
        self.forbidden = self.forbidden + other.forbidden
        # 去重
        self.forbidden = list(set(self.forbidden))

        return self


class UserScope(Scope):
    allow_api = ['v1.user+get_user', 'v1.user+delete_user', 'v1.user+update_user']
    forbidden = ['v1.user+super_get_user', 'v1.user+super_delete_user']

    def __init__(self):
        self + AdminScope()


class AdminScope(Scope):
    allow_api = ['v1.user+super_get_user', 'v1.user+super_delete_user']
    allow_module = ['v1.user']

    def __init__(self):
        pass
        # self + UserScope()


class SuperScope(Scope):
    allow_api = ['v1.su1']
    allow_module = ['v1.user']

    def __init__(self):
        self + UserScope() + AdminScope()


def is_in_scope(scope, endpoint):
    """判断视图函数是否在权限里面"""
    scope = globals()[scope]()
    splits = endpoint.split('+')
    red_name = splits[0]

    if endpoint in scope.forbidden:
        return True

    if endpoint in scope.allow_api:
        return True

    if red_name in scope.allow_module:
        return True

    return False



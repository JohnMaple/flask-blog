# -*- coding: utf-8 -*-
"""
    @description: 用户视图模型
"""

__author__ = 'Henry'


class ProfileViewModel:

    def __init__(self, profile):
        self.id = profile.id
        self.username = profile.username
        self.nickname = profile.nickname
        self.email = profile.email
        self.avatar = profile.avatar
        self.last_login_datetime = profile.last_login_datetime or ''
        self.last_login_ip = profile.last_login_ip or ''
        self.status = profile.status
        self.roles = ['admin']


class ProfileCollection:
    pass




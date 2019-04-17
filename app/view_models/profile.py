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
    pass


class ProfileCollection:
    pass




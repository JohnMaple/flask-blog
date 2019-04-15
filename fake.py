# -*- coding: utf-8 -*-
"""
    @description: 
    @copyright: (c) 2019/3/28 18:17 by Henry.
"""
from datetime import datetime

__author__ = 'Henry'


from app import create_app
from app.models.base import db
from app.models.admin import Admin

app = create_app()
with app.app_context():
    with db.auto_commit():
        # 创建一个超级管理员
        user = Admin()
        user.nickname = 'Admin'
        user.username = 'admin'
        user.password = '123456'
        user.email = '934879001@qq.com'
        db.session.add(user)

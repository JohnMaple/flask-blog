# -*- coding: utf-8 -*-
"""
    @description: 
"""
from flask import Blueprint

from app.api.admin import token, user, profile

__author__ = 'Henry'


def create_blueprint_admin():
    bp_admin = Blueprint('admin', __name__)

    # 视图注册
    token.api.register(bp_admin)
    profile.api.register(bp_admin)
    user.api.register(bp_admin)

    return bp_admin




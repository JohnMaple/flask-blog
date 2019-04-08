# -*- coding: utf-8 -*-
"""
    @description: 
"""
from flask import Blueprint

from app.api.admin import user

__author__ = 'Henry'


def create_blueprint_admin():
    bp_admin = Blueprint('admin', __name__)

    # 视图注册
    user.api.register(bp_admin)

    return bp_admin




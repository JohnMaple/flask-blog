# -*- coding: utf-8 -*-
"""
    @description: 
"""
from flask import Blueprint

from app.api.v1 import user

__author__ = 'Henry'


def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)

    # 视图注册
    user.api.register(bp_v1)

    return bp_v1



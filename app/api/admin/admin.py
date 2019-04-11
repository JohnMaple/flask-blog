# -*- coding: utf-8 -*-
"""
    @description: 
"""
from flask import jsonify

from app.libs.auth import auth
from app.libs.redprint import Redprint

__author__ = 'Henry'

api = Redprint('admin')


@api.route('', methods=['GET'])
@auth.login_required
def get_user():

    return jsonify()



# -*- coding: utf-8 -*-
"""
    @description: 
"""
import json

from flask import g, jsonify, current_app

from app.libs.auth_admin import auth
from app.libs.error_code import Success
from app.libs.redprint import Redprint
from app.models.admin import Admin
from app.view_models.profile import ProfileViewModel

__author__ = 'Henry'

api = Redprint('profile')


@api.route('', methods=['GET'])
@auth.login_required
def get_user():
    uid = g.admin.uid
    profile = Admin.query.get_or_404(uid)
    data = ProfileViewModel(profile)

    return Success(data=data)



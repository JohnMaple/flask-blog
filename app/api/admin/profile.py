# -*- coding: utf-8 -*-
"""
    @description: 
"""
from flask import g

from app.libs.auth_admin import auth
from app.libs.error_code import Success
from app.libs.redprint import Redprint
from app.models.admin import Admin

__author__ = 'Henry'

api = Redprint('profile')


@api.route('', methods=['GET'])
@auth.login_required
def get_user():
    uid = g.admin.uid
    profile = Admin.query.get_or_404(uid)

    return Success(data=profile)



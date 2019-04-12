# -*- coding: utf-8 -*-
"""
    @description: 后台多重API验证
"""
from collections import namedtuple

from flask import current_app, g, request
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth, MultiAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired

from app.libs.error_code import AuthFailed, Forbidden
from app.libs.scope import is_in_scope
from app.models.admin import Admin

__author__ = 'Henry'


basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()
auth = MultiAuth(basic_auth, token_auth)

User = namedtuple('User', ['uid', 'ac_type', 'scope'])


@basic_auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    user = verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        user = Admin.query.filter_by(username=username_or_token).first()
        if not user or not user.check_password(password):
            return False
    g.user = user
    return True


@token_auth.verify_token
def verify_token(token):

    user_info = verify_auth_token(token)

    if not user_info:
        return False
    else:
        g.user = user_info
        return True


def verify_auth_token(token):
    """验证token"""
    serializer = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = serializer.loads(token)
    except BadSignature:
        raise AuthFailed(msg='token is invalid', error_code=1002)
    except SignatureExpired:
        raise AuthFailed(msg='token is expired', error_code=1003)

    uid = data['uid']
    ac_type = data['type']
    scope = data['scope']

    # request 可以确认视图函数
    if not is_in_scope(scope, request.endpoint):
        raise Forbidden()

    return User(uid, ac_type, scope)




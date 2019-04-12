# -*- coding: utf-8 -*-
"""
    @description: 
"""
from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired

from app.libs.enums import ClientTypeEnum
from app.libs.redis import Redis
from app.libs.redprint import Redprint
from app.libs.auth import auth
from app.libs.utils import generate_nonce_str
from app.models.admin import Admin
from app.validators.forms import ClientForm

import redis

__author__ = 'Henry'


api = Redprint('token')


@api.route('', methods=['POST'])
def get_token():
    form = ClientForm().validate_for_api()

    promise = {
        ClientTypeEnum.USER_NAME: Admin.verify
    }

    # 身份验证
    identity = promise[ClientTypeEnum(form.type.data)](form.account.data, form.secret.data)

    expiration = current_app.config['TOKEN_EXPIRATION']

    # 生成token, 加盐生成token，hash存储redis，注销时，清空salt即可
    token = generate_auth_token(identity['uid'], form.type.data, identity['scope'], expiration)

    

    pass


@api.route('', methods=['DELETE'])
@auth.login_required
def revoke_toke():
    pass


def generate_auth_token(uid, ac_type, scope=None, expiration=7200):
    """
    生成令牌，保存到redis
    :param uid: 用户id
    :param ac_type: 客户端类型
    :param scope: 权限
    :param expiration: 有效期
    :return: token
    """

    salt = generate_nonce_str()
    serializer = Serializer(current_app.config['SECRET_KEY'], expiration, salt=salt)
    token = serializer.dumps({'uid': uid, 'type': ac_type.value, 'scope': scope})

    # 保存到redis
    redis = Redis()
    name = current_app.config['REDIS_KEY_PREFIX'] + 'admin_token'
    redis.hset(name, token, salt)

    return token




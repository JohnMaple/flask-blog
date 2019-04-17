# -*- coding: utf-8 -*-
"""
    @description: 
"""
from flask import current_app, jsonify, g
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired

from app.libs.enums import ClientTypeEnum
from app.libs.error_code import Success, DeleteSuccess
from app.libs.redis import Redis
from app.libs.redprint import Redprint
from app.libs.auth_admin import auth
from app.libs.utils import generate_nonce_str
from app.models.admin import Admin
from app.validators.forms import AdminLoginForm

__author__ = 'Henry'


api = Redprint('token')


@api.route('', methods=['POST'])
def get_token():
    form = AdminLoginForm().validate_for_api()

    promise = {
        ClientTypeEnum.USER_NAME: Admin.verify
    }

    # 身份验证
    identity = promise[ClientTypeEnum(form.type.data)](form.username.data, form.password.data)

    expiration = current_app.config['TOKEN_EXPIRATION']

    # 生成token, 加盐生成token，hash存储redis，注销时，清空salt即可
    token = generate_auth_token(identity['uid'], form.type.data, expiration)

    # 更新登录时间和ip

    data = dict(token=token.decode('ascii'))

    return Success(data=data)


@api.route('', methods=['DELETE'])
@auth.login_required
def revoke_toke():
    # 解析token获取用户信息
    if g.admin:
        redis = Redis()
        redis_name = current_app.config['REDIS_KEY_PREFIX'] + 'admin_token'
        redis.hdel(redis_name, g.admin_token)

    return DeleteSuccess(msg='注销成功')


def generate_auth_token(uid, ac_type, expiration=7200):
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
    token = serializer.dumps({'uid': uid, 'type': ac_type.value})

    # 保存到redis
    redis = Redis()
    redis_name = current_app.config['REDIS_KEY_PREFIX'] + 'admin_token'
    redis.hset(redis_name, token, salt)

    return token




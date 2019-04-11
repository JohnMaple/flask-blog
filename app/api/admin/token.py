# -*- coding: utf-8 -*-
"""
    @description: 
"""
from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired

from app.libs.enums import ClientTypeEnum
from app.libs.redprint import Redprint
from app.libs.auth import auth
from app.models.admin import Admin
from app.validators.forms import ClientForm

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

    secret_key = current_app.config['SECRET_KEY']

    expiration = current_app.config['TOKEN_EXPIRATION']

    # 生成token, 保存到缓存里面
    token = Admin.generate_auth_token(secret_key, expiration)

    pass


@api.route('', methods=['DELETE'])
@auth.login_required
def revoke_toke():
    pass


def generate_auth_token(uid, ac_type, scope=None, expiration=7200):
    """
    生成令牌
    :param uid: 用户id
    :param ac_type: 客户端类型
    :param scope: 权限
    :param expiration: 有效期
    :return: token
    """
    serializer = Serializer(current_app.config['SECRET_KEY'], expiration)

    return serializer.dumps({'uid': uid, 'type': ac_type.value, 'scope': scope})




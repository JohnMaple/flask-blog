# -*- coding: utf-8 -*-
"""
    @description:
"""
from sqlalchemy import Column, Integer, String, SmallInteger, orm
from werkzeug.security import generate_password_hash, check_password_hash

from app.libs.error_code import NotFound, AuthFailed
from app.models.base import Base, db

__author__ = 'Henry'


class User(Base):
    __abstract__ = True
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, comment='id')
    nickname = Column(String(24), nullable=False, comment='昵称')
    email = Column(String(24), unique=True, nullable=False, comment='邮箱')
    phone = Column(String(13), unique=True, nullable=False, comment='手机号')
    auth = Column(SmallInteger, default=1, comment='权限，超级管理员或普通用户')
    _password = Column('password', String(128), nullable=False, comment='密码')

    # flask 通过元类创建对象，不会自动执行构造函数
    @orm.reconstructor
    def __init__(self):
        self.fields = ['id', 'email', 'nickname', 'auth']

    # def keys(self):
    #     return ['id', 'email', 'nickname', 'auth']

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    @staticmethod
    def register_by_email(nickname, account, secret):
        with db.auto_commit():
            user = User()
            user.nickname = nickname
            user.email = account
            user.password = secret
            db.session.add(user)

    @staticmethod
    def verify(email, password):
        user = User.query.filter_by(email=email).first_or_404()
        # if not user:
        #     raise NotFound(msg='用户不存在')
        if not user.check_password(password):
            raise AuthFailed()

        # 可以使用redis存储接口权限
        scope = 'AdminScope' if user.auth == 2 else 'UserScope'

        return {'uid': user.id, 'scope': scope}

    def check_password(self, raw):
        if not self._password:
            return False
        return check_password_hash(self._password, raw)




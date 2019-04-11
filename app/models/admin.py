# -*- coding: utf-8 -*-
"""
    @description: 
"""
from sqlalchemy import Column, Integer, String, SmallInteger, orm, DateTime
from werkzeug.security import generate_password_hash, check_password_hash

from app.libs.error_code import AuthFailed
from app.models.base import Base


__author__ = 'Henry'


class Admin(Base):
    __tablename__ = 'admin'
    id = Column(Integer, primary_key=True, autoincrement=True, comment='id')
    username = Column(String(24), nullable=False, default='', comment='用户名')
    nickname = Column(String(50), nullable=False, default='', comment='昵称')
    _password = Column('password', String(128), nullable=False, comment='密码')
    avatar = Column(String(100), nullable=False, default='', comment='头像')
    email = Column(String(100), nullable=False, default='', comment='邮箱')
    token = Column(String(100), nullable=False, default='', comment='token')
    token_expiration = Column(DateTime)
    created_at = Column('created_at', Integer, comment='创建时间')
    updated_at = Column('updated_at', Integer, comment='更新时间')
    status = Column(SmallInteger, default=1, comment='状态,0:删除,1:正常,2:隐藏')

    # flask 通过元类创建对象，不会自动执行构造函数
    @orm.reconstructor
    def __init__(self):
        self.fields = ['id', 'username', 'nickname', 'avatar', 'email', 'token', 'token_expiration']

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        """验证密码"""
        if not self._password:
            return False

        return check_password_hash(self._password, raw)

    @staticmethod
    def verify(username, password):
        user = Admin.query.filter_by(username=username).first_or_404()

        if not user.check_password(password):
            raise AuthFailed()










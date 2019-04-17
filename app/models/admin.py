# -*- coding: utf-8 -*-
"""
    @description: 
"""
from datetime import datetime

from sqlalchemy import Column, Integer, String, SmallInteger, orm, DateTime
from werkzeug.security import generate_password_hash, check_password_hash

from app.libs.error_code import AuthFailed
from app.models.base import Base


__author__ = 'Henry'


class Admin(Base):
    __tablename__ = 'tim_admin'
    id = Column(Integer, primary_key=True, autoincrement=True, comment='id')
    username = Column(String(24), unique=True, nullable=False, default='', comment='用户名')
    nickname = Column(String(50), nullable=False, default='', comment='昵称')
    _password = Column('password', String(128), nullable=False, comment='密码')
    avatar = Column(String(100), nullable=False, default='', comment='头像')
    email = Column(String(100), nullable=False, default='', comment='邮箱')
    last_login_ip = Column(String(50), nullable=False, default='', comment='最后登录的ip')
    last_login_at = Column('last_login_at', Integer, comment='最后登录时间')
    created_at = Column('created_at', Integer, comment='创建时间')
    updated_at = Column('updated_at', Integer, comment='更新时间')
    status = Column(SmallInteger, default=1, comment='状态,0:删除,1:正常,2:隐藏')

    # flask 通过元类创建对象，不会自动执行构造函数
    @orm.reconstructor
    def __init__(self):
        super().__init__()
        # json序列化的时候用到
        self.fields = ['id', 'username', 'nickname', 'avatar', 'email', 'created_at', 'updated_at']

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    @property
    def last_login_datetime(self):
        if self.last_login_at:
            return datetime.fromtimestamp(self.last_login_at)
        else:
            None

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

        return {'uid': user.id}










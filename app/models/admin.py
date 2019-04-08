# -*- coding: utf-8 -*-
"""
    @description: 
"""
from sqlalchemy import Column, Integer, String, SmallInteger, orm, DateTime
from werkzeug.security import generate_password_hash

from app.models.base import Base


__author__ = 'Henry'


class Admin(Base):
    __tablename__ = 'admin'
    id = Column(Integer, primary_key=True, autoincrement=True, comment='id')
    username = Column(String(24), nullable=False, default='', comment='用户名')
    nickname = Column(String(50), nullable=False, default='', comment='昵称')
    _password = Column('password', String(128), nullable=False, comment='密码')
    salt = Column(String(30), nullable=False, default='', comment='密码盐')
    avatar = Column(String(100), nullable=False, default='', comment='头像')
    email = Column(String(100), nullable=False, default='', comment='邮箱')
    created_at = Column('created_at', Integer, comment='创建时间')
    updated_at = Column('updated_at', Integer, comment='更新时间')
    status = Column(SmallInteger, default=1, comment='状态,0:删除,1:正常,2:隐藏')

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)





# -*- coding: utf-8 -*-
"""
    @description: 
"""
from sqlalchemy import Column, Integer, String, ForeignKey, SmallInteger, Text

from app.models.base import Base

__author__ = 'Henry'


class AdminLog(Base):
    __tablename__ = 'tim_admin_log'
    id = Column(Integer, primary_key=True, autoincrement=True, comment='id')
    admin_id = Column(Integer, ForeignKey('tim_admin.id'))
    username = Column(String(24), nullable=False, default='', comment='管理员')
    ip = Column(String(50), nullable=False, default='', comment='登录的ip')
    useragent = Column(String(255), nullable=False, default='', comment='User-Agent')
    title = Column(String(100), nullable=False, default='', comment='操作标题')
    content = Column(Text, default='', comment='日志内容')
    created_at = Column('created_at', Integer, comment='创建时间')
    updated_at = Column('updated_at', Integer, comment='更新时间')
    status = Column(SmallInteger, default=1, comment='状态,0:删除,1:正常,2:隐藏')




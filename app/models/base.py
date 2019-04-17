# -*- coding: utf-8 -*-
"""
    @description:
"""
from datetime import datetime
from contextlib import contextmanager

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery
from sqlalchemy import Column, Integer, SmallInteger

from app.libs.error_code import NotFound

__author__ = 'Henry'


class SQLAlchemy(_SQLAlchemy):

    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e


class Query(BaseQuery):
    """
    改写内置的方法
    """
    def filter_by(self, **kwargs):
        if 'status' not in kwargs.keys():
            kwargs['status'] = 1

        return super(Query, self).filter_by(**kwargs)

    def get_or_404(self, ident):
        rv = self.get(ident)
        if not rv:
            raise NotFound()
        return rv

    def first_or_404(self):
        rv = self.first()
        if not rv:
            raise NotFound()
        return rv


db = SQLAlchemy(query_class=Query)


class Base(db.Model):
    __abstract__ = True  # 不会创建base表
    created_at = Column('created_at', Integer)
    updated_at = Column('updated_at', Integer)
    status = Column(SmallInteger, default=1)
    fields = []

    def __init__(self):
        self.created_at = int(datetime.now().timestamp())
        self.updated_at = int(datetime.now().timestamp())

    @property
    def create_datetime(self):
        if self.created_at:
            return datetime.fromtimestamp(self.created_at)
        else:
            None

    @property
    def update_datetime(self):
        if self.updated_at:
            return datetime.fromtimestamp(self.updated_at)
        else:
            None

    def set_attrs(self, attrs_dict):
        """
        前端表单自动填充对应的表字段
        :param attrs_dict:
        :return:
        """
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)

    def delete(self):
        self.status = 0

    def __getitem__(self, item):
        return getattr(self, item)

    # dict() 会自动调用keys方法，如何获取全部的fields？定义返回字典中的键
    def keys(self):
        return self.fields

    def hide(self, *keys):
        for key in keys:
            self.fields.remove(key)
        return self

    def append(self, *keys):
        for key in keys:
            self.fields.append(key)
        return self



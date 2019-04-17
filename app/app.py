# -*- coding: utf-8 -*-
"""
    @description: 
"""
import uuid

from flask._compat import text_type
from werkzeug.http import http_date

__author__ = 'Henry'


from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder
from datetime import date, datetime

from app.libs.error_code import ServerError

__author__ = 'Henry'


class JSONEncoder(_JSONEncoder):
    def default(self, o):
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            return dict(o)
        if isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        if isinstance(o, datetime):
            return o.strftime("%Y-%m-%d %H-%M-%S")
        raise ServerError()


class Flask(_Flask):
    json_encoder = JSONEncoder


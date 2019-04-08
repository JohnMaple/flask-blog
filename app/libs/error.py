# -*- coding: utf-8 -*-
"""
    @description: 错误异常
"""
from flask import request, json
from werkzeug.exceptions import HTTPException

__author__ = 'Henry'


class APIException(HTTPException):
    code = 500
    msg = 'sorry, we make a mistake (*￣︶￣)!'
    error_code = 999
    data = None
    extend = None

    def __init__(self, msg=None, code=None, error_code=None, headers=None, data=None, extend=None):
        if code:
            self.code = code
        if error_code:
            self.error_code = error_code
        if msg:
            self.msg = msg
        if data:
            self.data = data
        if extend:
            self.extend = extend

        super(APIException, self).__init__(msg, None)

    def get_body(self, environ=None):
        body = dict(
            msg=self.msg,
            error_code=self.error_code,
            request=request.method + ' ' + self.get_url_no_param()  # 'POST v1/client/register'
        )

        if self.data:
            body.update(dict(data=self.data))

        if self.extend and isinstance(self.extend, dict):
            body.update(self.extend)

        text = json.dumps(body)
        return text

    def get_headers(self, environ=None):
        """Get a list of headers."""
        return [("Content-Type", "application/json")]

    @staticmethod
    def get_url_no_param():
        full_path = str(request.full_path)
        main_path = full_path.split('?')
        return main_path[0]




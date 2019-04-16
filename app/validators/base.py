# -*- coding: utf-8 -*-
"""
    @description: 
"""
from flask import request
from wtforms import Form

from app.libs.error_code import ParameterException

__author__ = 'Henry'


class BaseForm(Form):

    def __init__(self):
        # 表单数据
        form_data = request.form
        # 获取body参数, 解析错误返回None
        data = request.get_json(silent=True)
        # 获取查询参数
        args = request.args.to_dict()
        super().__init__(formdata=form_data, data=data, **args)

    def validate_for_api(self):
        valid = super().validate()

        if not valid:
            # 所有错误信息存在form.errors
            raise ParameterException(msg=self.get_errors())

        return self

    def get_errors(self):
        errors = ''
        for v in self.errors.values():
            errors += ' '.join(v)
        return errors




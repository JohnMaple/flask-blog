# -*- coding: utf-8 -*-
"""
    @description: 初始化项目，加载配置项，注册蓝图、数据库等
"""
import os
from flask import Flask
from dotenv import load_dotenv
from app.models.base import db

__author__ = 'Henry'

# 加载.env文件到环境变量
load_dotenv(os.path.join(os.path.abspath(os.path.dirname(__file__)), '.env'))


def register_blueprint(app):
    """ 注册蓝图 """
    pass


def register_plugins(app):
    # 注册模型
    db.init_app(app)


def create_app():
    """ 工厂模式，创建flask实例 """

    app = Flask(__name__)

    # 生产开发环境
    app_env = os.environ.get('APP_ENV').title() + 'Config'

    # 加载配置项
    app.config.from_object('app.config.secure.' + app_env)
    app.config.from_object('app.config.settings')

    print(os.getenv('SQLALCHEMY_BINDS'))

    # 注册蓝图
    register_blueprint(app)

    # 注册插件
    register_plugins(app)

    return app


# -*- coding: utf-8 -*-
"""
    @description: 安全配置
"""
import os

__author__ = 'Henry'

# SCERET_KEY = os.urandom(24)
SECRET_KEY = '\x91\xb3\xe2-\xe678g\xc4\xd0^W\x8c=\x91rjfg%\x1d1\xbd\x8b>\xc6\xba\x98\xd8X$\xbf'

DB_CONNECTION = os.environ.get('DB_CONNECTION', 'mysql')
DB_HOST = os.environ.get('DB_HOST', '127.0.0.1')
DB_PORT = os.environ.get('DB_PORT', '3306')
DB_DATABASE = os.environ.get('DB_DATABASE', 'flask')
DB_USERNAME = os.environ.get('DB_USERNAME', 'root')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'root')


class Config:
    DEBUG = False
    TESTING = False

    # 数据库配置
    # SQLALCHEMY_DATABASE_URI = DB_CONNECTION + '+cymysql://' + DB_USERNAME + ':' + DB_PASSWORD + '@' + DB_HOST + ':'+ DB_PORT + '/' + DB_DATABASE
    SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:root@localhost:3306/flask_blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_TEARDOWN = True


class ProductionConfig(Config):
    DEBUG = os.environ.get('DEBUG', False)

    # 数据库配置
    SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:root@localhost:3306/flask_restful'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_TEARDOWN = True


class DevelopmentConfig(Config):
    DEBUG = os.environ.get('DEBUG', True)


class TestingConfig(Config):
    TESTING = True



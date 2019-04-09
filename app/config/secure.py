# -*- coding: utf-8 -*-
"""
    @description: 安全配置
"""
import os

__author__ = 'Henry'


class Config:
    DEBUG = False
    TESTING = False

    # SCERET_KEY = os.urandom(24)
    SECRET_KEY = '\x91\xb3\xe2-\xe678g\xc4\xd0^W\x8c=\x91rjfg%\x1d1\xbd\x8b>\xc6\xba\x98\xd8X$\xbf'

    # 数据库配置
    SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:root@localhost:3306/flask_blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_TEARDOWN = True

    # 缓存
    CACHE_TYPE = os.getenv('CACHE_TYPE', 'simple')
    CACHE_KEY_PREFIX = os.getenv('CHCHE_KEY_PREFIX', 'tim_')
    CACHE_REDIS_HOST = os.getenv('CACHE_REDIS_HOST', 'localhost')
    CACHE_REDIS_PORT = int(os.getenv('CACHE_REDIS_PORT', 6379))
    CACHE_REDIS_PASSWORD = os.getenv('CACHE_REDIS_PASSWORD', '')
    CACHE_REDIS_DB = os.getenv('CACHE_REDIS_DB', '')


class ProductionConfig(Config):
    DEBUG = True if 'true' == os.getenv('DEBUG') else False

    # 数据库配置
    SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:root@localhost:3306/flask_blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_TEARDOWN = True


class DevelopmentConfig(Config):
    DEBUG = True if 'true' == os.getenv('DEBUG') else False


class TestingConfig(Config):
    TESTING = True



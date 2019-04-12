# -*- coding: utf-8 -*-
"""
    @description: 
"""
import redis
from flask import current_app


__author__ = 'Henry'


class Redis:

    def __init__(self, host='127.0.0.1', port=6379, db=0, password=None):
        base_config = current_app.config.copy()

        config = {
            'host': host or base_config['REDIS_HOST'],
            'password': password or base_config['REDIS_PASSWORD'],
            'port': port or base_config['REDIS_PORT'],
            'db': db or base_config['REDIS_DB'],
            'max_connections': 15,
        }

        pool = redis.BlockingConnectionPool(**config)

        self.__conn = redis.StrictRedis(connection_pool=pool)

    def __getattr__(self, command):
        def _(*args):
            return getattr(self.__conn, command)(*args)  # 重新组装方法调用

        return _



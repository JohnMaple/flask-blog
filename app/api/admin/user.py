# -*- coding: utf-8 -*-
"""
    @description:
"""
from flask import jsonify, session

from app import cache
from app.libs.redis import Redis
from app.libs.redprint import Redprint

__author__ = 'Henry'

api = Redprint('user')


@api.route('', methods=['GET'])
def get_user():
    """
    获取用户信息，可以使用view_model,严谨的restful没必要
    :param uid:
    :return:
    """
    redis = Redis()
    cache.set('name', 'xiaoming', timeout=30)
    cache.set('person', {'name': 'aaa', 'age': 20})
    name = cache.get('name')
    cache.set_many([('name1', 'hhh'), ('name2', 'jjj')])
    session['username'] = 'john'
    data = dict(
        name=cache.get('name'),
        person=cache.get('person'),
        username=session.get('username')
    )

    redis.set('r_name', 'john')
    r_name = redis.get('r_name')

    data = dict(
        name=r_name.decode('utf-8')
    )

    return jsonify(data)




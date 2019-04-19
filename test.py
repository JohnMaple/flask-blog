# -*- coding: utf-8 -*-
"""
    @description: 
"""
import json

__author__ = 'Henry'


class Grade:
    def __init__(self):
        self.grade = '1'


class User:
    def __init__(self):
        grade = Grade()
        self.name = 'john'
        self.age = 18
        self.gender = 'male'
        self.grade = Grade()


o = User()

print(type(o.__dict__))
print(type(json.dumps(o, default=lambda obj: obj.__dict__)))



# -*- coding: utf-8 -*-
"""
    @description: 邮件
"""
from threading import Thread
from flask import current_app, render_template
from flask_mail import Message

from app import mail


__author__ = 'Henry'


def send_email(to, subject, template, **kwargs):
    """
    Python有标准库提供的email接口，参数过多，使用不方便
    :param to:
    :param subject:
    :param template:
    :param kwargs:
    :return:
    """
    msg = Message()
    msg = Message(current_app.config['MAIL_SUBJECT_PREFIX'] + ' ' + subject, sender=current_app.config['MAIL_USERNAME'], recipients=[to])
    msg.html = render_template(template, **kwargs)

    app = current_app._get_current_object()
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()


def send_async_email(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            pass



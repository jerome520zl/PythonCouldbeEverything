# -*- coding: utf-8 -*-
"""
Created by hushiwei on 16-12-21.
"""
'''
pip install forgerypy
ForgeryPy is an easy to use forged data generator.
https://github.com/tomekwojcik/ForgeryPy
'''
import forgery_py
import logging
import logstash
logger=logging.getLogger("python-logstash-logger")
logger.setLevel(logging.INFO)
logger.addHandler(logstash.LogstashHaddler('10.10.25.13',4567))

logger.error('python-logstash: test logstash error message.')
logger.info('python-logstash: test logstash info message.')
logger.warning('python-logstash: test logstash warning message.')

address = forgery_py.address.street_address()
print address


color = forgery_py.basic.hex_color()
print color

des = forgery_py.currency.description()
print des

t=forgery_py.date.date()
print t

email=forgery_py.internet.email_address()
print email

title=forgery_py.lorem_ipsum.title()
print title

name=forgery_py.name.full_name()
print name

langu=forgery_py.personal.language()
print langu

#!/usr/bin/env python
# -*- coding:utf-8 -*-

from random import randint

def mysql_modsecurityversioned(payload):
	# -- mysql -- #
	_payload = payload
	if payload:
		postfix = ''
		for comment in ('#','--','/*'):
			if comment in payload:
				postfix = payload[payload.find(comment):]
				payload = payload[:payload.find(comment)]
				break
		if ' ' in payload:
			_payload = "%s /*!30%s%s*/%s"%(
				payload[:payload.find(' ')],randint(100,999),payload[payload.find(' ')+1:],postfix)
	return _payload
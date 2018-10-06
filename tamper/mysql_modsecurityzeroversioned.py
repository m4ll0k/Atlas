#!/usr/bin/env python
# -*- coding:utf-8 -*-


def mysql_modsecurityzeroversioned(payload):
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
			_payload = "%s /*!00000%s*/%s"%(payload[:payload.find(' ')],payload[payload.find(' ')+1:],
				postfix)
	return _payload
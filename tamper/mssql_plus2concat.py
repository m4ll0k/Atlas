#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def mssql_plus2concat(payload):
	# -- mssql -- #
	_payload = payload
	if payload:
		match = re.search(r'CHAR\(\d+\)\+',payload,re.I)
		if match:
			start = payload[:payload.index(match.group())].split('(')[0]
			_payload = payload[payload.index(match.group()):]
			find = re.findall(r'CHAR\(\d+\)[\+]*',payload,re.I)
			for statement in find:
				if '+' in statement:
					_payload = _payload.replace(statement,statement.split('+')[0]+',')
			_payload = "%sCONCAT(%s"%(start,_payload)
	return _payload
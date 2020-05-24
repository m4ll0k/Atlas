#!/usr/bin/env python
# -*- coding:utf-8 -*-

def general_space2mssqlhash(payload):
	# -- general -- #
	_payload = ""
	if payload:
		for i in range(len(payload)):
			if payload[i].isspace():
				_payload += "%23%0A"
			elif payload[i] == '#' or payload[i:i+3]== '-- ':
				_payload += payload[i:]
				break
			else:
				_payload+=payload[i]
	return _payload
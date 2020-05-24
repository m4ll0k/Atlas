#!/usr/bin/env python
# -*- coding:utf-8 -*-

def mysql_space2mysqldash(payload):
	# -- mysql -- # 
	_payload = payload
	if payload:
		_payload = ""
		for i in range(len(payload)):
			if payload[i].isspace():
				_payload+="--%0A"
			elif payload[i]=='#' or payload[i:i+3]=='-- ':
				_payload+=payload[i:]
				break
			else:
				_payload += payload[i]
	return _payload
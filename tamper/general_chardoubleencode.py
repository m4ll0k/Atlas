#!/usr/bin/env python
# -*- coding:utf-8 -*-

import string

def general_chardoubleencode(payload):
	# -- generic -- #
	_payload = payload 
	if payload:
		_payload = ""
		i = 0
		while i < len(payload):
			if payload[i] == '%' and(i<len(payload) - 2)and payload[i+1:i+2] in string.hexdigits and payload[i+2:i+3] in string.hexdigits:
				_payload += '%%25%s'%payload[i+1:i+3]
				i+=3
			else:
				_payload += '%%25%.2X'%ord(payload[i])
				i += 1
	return _payload
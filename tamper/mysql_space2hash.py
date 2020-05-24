#!/usr/bin/env python
# -*- coding:utf-8 -*-

import string
import random

def mysql_space2hash(payload):
	# -- mysql -- #
	_payload = ""
	if payload:
		for i in range(len(payload)):
			if payload[i].isspace():
				randomStr = ''.join(random.choice(string.ascii_uppercase + 
					string.ascii_lowercase) for _ in range(random.randint(6,12)))
				_payload += "%%23%s%%0A"%randomStr
			elif payload[i] == '#' or payload[i:i+3] == '-- ':
				_payload += payload[i:]
				break
			else:
				_payload += payload[i]
	return _payload
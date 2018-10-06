#!/usr/bin/env python
# -*- coding:utf-8 -*-

import string

def general_overlongutf8(payload):
	# -- general -- #
	_payload = payload
	if payload:
		i = 0
		_payload = ""
		while i < len(payload):
			if payload[i] == '%' and(i<len(payload)-2)and payload[i+1:i+2] in string.hexdigits and payload[i+2:i+3] in string.hexdigits:
				_payload += payload[i:i+3]
				i += 3
			else:
				if payload[i] not in (string.ascii_letters+string.digits):
					_payload += "%%%.2X%%%.2X"%(0xc0+(ord(payload[i])>>6),0x80+(ord(payload[i])&0x3f))
				else:
					_payload += payload[i]
				i += 1
	return _payload
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def mysql_hex2char(payload):
	# -- MYSQL 4, 5.0 and 5.5 -- # 
	_payload = payload
	if payload:
		for match in re.finditer(r"\b0x([0-9a-f]+)\b",_payload):
			if len(match.group(1))>2:
				results = "CONCAT(%s)"%(','.join('CHAR(%d)'%ord(_) for _ in match.group(1).decode('hex')))
			else:
				results = "CHAR(%d)"%ord(match.group(1).decode('hex'))
			_payload = _payload.replace(match.group(0),results)
	return _payload
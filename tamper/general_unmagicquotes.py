#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def general_unmagicquotes(payload):
	# -- general -- 
	_payload = payload
	if payload:
		found = False
		_payload = ""
		for i in range(len(payload)):
			if payload[i] == '\'' and not found:
				_payload += "%bf%27"
				found = True
			else:
				_payload += payload[i]
				continue
		if found:
			_ = re.sub(r"(?i)\s*(AND|OR)[\s(]+([^\s]+)\s*(=|LIKE)\s*\2", "",payload)
			if _ != _payload:
				_payload = _
				_payload += "-- "
			elif not any(_ in _payload for _ in('#','--','/*')):
				_payload += '-- '
	return _payload
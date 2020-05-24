#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def general_least(payload):
	# -- general -- #
	_payload = payload
	if payload:
		match = re.search(r"(?i)(\b(AND|OR)\b\s+)([^>]+?)\s*>\s*(\w+|'[^']+')",payload)
		if match:
			_ = "%sLEAST(%s,%s+1)=%s+1"%(match.group(1),
				match.group(3),match.group(4),match.group(4))
			_payload = _payload.replace(match.group(0),_)
	return _payload
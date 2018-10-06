#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def general_greatest(payload):
	# -- general -- #
	_payload = payload
	if payload:
		match = re.search(r"(?i)(\b(AND|OR)\b\s+)([^>]+?)\s*>\s*(\w+|'[^']+')",payload)
		if match:
			_ = "%sGREATEST(%s,%s+1)=%s"%(match.group(1),match.group(3),
				match.group(4),match.group(3))
			_payload = _payload.replace(match.group(0),_)
	return _payload
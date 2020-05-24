#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def general_between(payload):
	# -- generic -- #
	_payload = payload
	if payload:
		match = re.search(r"(?i)(\b(AND|OR)\b\s+)(?!.*\b(AND|OR)\b)([^>]+?)\s*>\s*([^>]+)\s*\Z",payload)
		if match:
			_ = "%s %s NOT BETWEEN 0 AND %s"%(
				match.group(2),match.group(4),match.group(5))
			_payload = _payload.replace(match.group(0),_)
		else:
			_payload = re.sub(r"\s*>\s*(\d+|'[^']+'|\w+\(\d+\))",r" NOT BETWEEN 0 AND \g<1>",payload)
		if _payload == payload:
			match = re.search(r"(?i)(\b(AND|OR)\b\s+)(?!.*\b(AND|OR)\b)([^=]+?)\s*=\s*(\w+)\s*",payload)
			if match:
				_ = "%s %s BETWEEN %s AND %s"%(
					match.group(2),match.group(4),match.group(5),match.group(5))
				_payload = _payload.replace(match.group(0),_)
	return _payload
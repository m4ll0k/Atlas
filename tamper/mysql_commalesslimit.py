#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def mysql_commalesslimit(payload):
	# -- mysql -- #
	_payload = payload
	match = re.search(r'(?i)LIMIT\s*(\d+),\s*(\d+)',payload)
	if match:
		_payload = _payload.replace(match.group(0),'LIMIT %s OFFSET %s'%(
			match.group(2),match.group(1))
		)
	return _payload
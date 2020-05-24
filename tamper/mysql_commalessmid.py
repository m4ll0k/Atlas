#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def mysql_commalessmid(payload):
	# -- mysql -- #
	_payload = payload 
	match = re.search(r'(?i)MID\((.+?)\s*,\s*(\d+)\s*\,\s*(\d+)\s*\)',payload)
	if match:
		_payload = _payload.replace(match.group(0),'MID(%s FROM %s FOR %s)'%(
			match.group(1),match.group(2),match.group(3))
		)
	return _payload
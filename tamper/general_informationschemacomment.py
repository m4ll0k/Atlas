#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def general_informationschemacomment(payload):
	# -- general -- #
	_payload = payload
	if payload:
		_payload = re.sub(r'(?i)(information_schema)\.',r'\g<1>/**/.',payload)
	return _payload
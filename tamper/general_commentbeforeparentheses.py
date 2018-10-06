#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def general_commentbeforeparentheses(payload):
	# -- general -- #
	_payload =payload
	if payload:
		_payload = re.sub(r'\b(\w+)\(',r'\g<1>/**/(',_payload)
	return _payload
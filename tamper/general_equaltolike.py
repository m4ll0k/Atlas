#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def general_equaltolike(payload):
	# -- general -- # 
	_payload = payload
	if payload:
		_payload = re.sub(r'\s*=\s*',' LIKE ',_payload)
	return _payload
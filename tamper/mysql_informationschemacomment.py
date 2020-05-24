#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def mysql_informationschemacomment(payload):
	# -- MYSQL -- # 
	_payload = payload
	if payload:
        # (?i) lowercase, \g<1> group 
		_payload = re.sub(r'(?i)(information_schema)\.','\g<1>/**/.',payload)
	return _payload
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def general_symboliclogical(payload):
	# -- general -- #
	_payload = payload
	if payload:
		_payload = re.sub(r"(?i)\bAND\b", "%26%26", re.sub(r"(?i)\bOR\b", "%7C%7C", payload))
	return _payload
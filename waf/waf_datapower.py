#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def waf_datapower(*_):
	'''IBM WebSphere DataPower (IBM)'''
	for item in _[0].items():
		if re.search(r'\A(OK|FAIL)',item[0] or '', re.I):
			return waf_datapower.__doc__
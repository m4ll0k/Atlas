#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def waf_webknight(*_):
	'''WebKnight Application Firewall (AQTRONIX)'''
	for item in _[0].items():
		if re.search('WebKnight',item[1] or '',re.I):
			return waf_webknight.__doc__
	if _[2]==999:return waf_webknight.__doc__
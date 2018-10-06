#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def waf_fortiweb(*_):
	'''FortiWeb Web Application Firewall (Fortinet)'''
	for item in _[0].items():
		if re.search(r'\AFORTIWAFSID=',item[1] or '',re.I):
			return waf_fortiweb.__doc__
	if all(_ in (_[1] or '') for _ in ('.fgd_icon','.blocked','.authenticate')):
		return waf_fortiweb.__doc__
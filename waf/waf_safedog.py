#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def waf_safedog(*_):
	'''Safedog Web Application Firewall (Safedog)'''
	for item in _[0].items():
		if re.search(r'WAF/2\.0|Safedog',item[1] or '',re.I):
			return waf_safedog.__doc__
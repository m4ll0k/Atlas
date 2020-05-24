#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def waf_safe3(*_):
	'''Safe3 Web Application Firewall'''
	for item in _[0].items():
		if re.search(r'Safe3WAF|Safe3 Web Firewall',item[1],re.I):
			return waf_safe3.__doc__
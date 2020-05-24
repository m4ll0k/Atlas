#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def waf_yunsuo(*_):
	'''Yunsuo Web Application Firewall (Yunsuo)'''
	for item in _[0].items():
		if re.search(r'yunsuo_session',item[1] or '',re.I):
			return waf_yunsuo.__doc__
	if re.search(r'\<img class\=\"yunsuologo\"',str(_[1]) or '',re.I):
		return waf_yunsuo.__doc__
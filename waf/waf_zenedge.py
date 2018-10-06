#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def waf_zenedge(*_):
	'''Zenedge Web Application Firewall (Zenedge)''' 
	for item in _[0].items():
		if _[2]>=400 and re.search(r'\AZENEDGE',item[1] or '',re.I):
			return waf_zenedge.__doc__
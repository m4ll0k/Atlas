#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def waf_hyperguard(*_):
	'''Hyperguard Web Applicatin Firewall (art of defence)'''
	for item in _[0].items():
		if re.search(r'\AODSESSION\=',item[1] or '',re.I) is not None:
			return waf_hyperguard.__doc__
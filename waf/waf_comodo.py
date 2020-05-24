#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def waf_comodo(*_):
	'''Comodo Web Application Firewall (Comodo)'''
	for item in _[0].items():
		if re.search(r'Protected by COMODO WAF',item[0] or '', re.I):
			return waf_comodo.__doc__
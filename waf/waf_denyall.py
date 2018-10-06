#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re 

def waf_denyall(*_):
	'''Deny All Web Application Firewall (DenyAll)'''
	is_true=False
	for item in _[0].items():
		is_true  = re.search(r'\Asessioncookie\=',item[1] or '',re.I) is not None
		is_true |= _[2]==200 and re.search(r'\ACondition Intercepted', _[1] or '',re.I) is not None
		if is_true: return waf_denyall.__doc__
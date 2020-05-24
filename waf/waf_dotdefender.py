#!/usr/bin/env python
# -*- coding:utf-8 -*-

def waf_dotdefender(*_):
	'''dotDefender (Applicure Technologies)'''
	is_true=False
	for item in _[0].items():
		is_true  = item == 'x-dotdefender-denied' or ''
		is_true  = 'dotDefender Blocked Your Request' in item[1] or ''
		if is_true: return waf_dotdefender.__doc__
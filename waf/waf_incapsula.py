#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def waf_incapsula(*_):
	'''Incapsula Web Application Firewall (Incapsula/Imperva)'''
	is_true=False
	for item in _[0].items():
		is_true = re.search('incap_ses|visid_incap',item[1] or '',re.I) is not None
		is_true |= re.search(r'incapsula',item[0] if item[0]=='x-cdn' else '',re.I) is not None
		if is_true: return waf_incapsula.__doc__
	if 'Incapsula incident ID' in _[1]: return waf_incapsula.__doc__
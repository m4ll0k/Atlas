#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def waf_jiasule(*_):
	'''Jiasule Web Application Firewall (Jiasule)'''
	is_true=False
	for item in _[0].items():
		is_true = re.search(r'jiasule-WAF|__jsluid=|jsl_tracking',
			item[1] or '',re.I) is not None
		if is_true: return waf_jiasule.__doc__
	if re.search(r'static\.jiasule\.com/static/js/http_error\.js',_[1] or '',re.I):
		return waf_jiasule.__doc__
	if _[2]==403 and 'notice-jiasule' in _[1]:
		return waf_jiasule.__doc__
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def waf_anquanbao(*_):
	'''Anquanbao Web Application Firewall (Anquanbao)'''
	is_true=False
	for item in _[0].items():
		is_true = re.search(r'MISS',item[1] if item[0] == 'x-powered-by-anquanbao' else '',re.I) is not None
		if is_true:return waf_anquanbao.__doc__
	is_true=_[2]==405 and any(_ in(_[1],'')for _ in("/aqb_cc/error/", "hidden_intercept_time"))
	if is_true:return waf_anquanbao.__doc__
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def waf_360(*_):
	'''360 Web Application Firewall (360)'''
	is_true = False
	for item in _[0].items():
		is_true|=re.search(r'wangzhan\.360\.cn',item[1],re.I)is not None
		if is_true:return waf_360.__doc__
	is_true|=_[2]==493 and "/wzws-waf-cgi/" in(_[1],'')
	if is_true:return waf_360.__doc__
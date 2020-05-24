#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def waf_baidu(*_):
	'''Yunjiasu Web Application Firewall (Baidu)'''
	is_true=False
	for item in _[0].items():
		is_true=re.search('fhl',item[1] or "",re.I) is not None
		is_true|=re.search(r'yunjiasu-nginx',item[1] or "",re.I) is not None
		if is_true:return waf_baidu.__doc__
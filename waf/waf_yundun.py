#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def waf_yundun(*_):
	'''Yundun Web Application Firewall (Yundun)'''
	for item in _[0].items():
		if re.search(r'yundun',item[1] or '',re.I):
			return waf_yundun.__doc__
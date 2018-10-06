#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def waf_newdefend(*_):
	'''Newdefend Web Application Firewall (Newdefend)'''
	for item in _[0].items():
		if re.search('newdefend',item[1] or '',re.I):
			return waf_newdefend.__doc__
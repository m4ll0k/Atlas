#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def waf_nsfocus(*_):
	'''NSFOCUS Web Application Firewall (NSFOCUS)'''
	for item in _[0].items():
		if re.search('NSFocus',item[1] or '',re.I):
			return waf_nsfocus.__doc__
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def waf_profense(*_):
	'''Profense Web Application Firewall (Armorlogic)'''
	for item in _[0].items():
		if re.search(r'\APLBSID\=|Profense',item[1] or '',re.I):
			return waf_profense.__doc__
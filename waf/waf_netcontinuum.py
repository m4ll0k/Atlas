#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def waf_netcontinuum(*_):
	'''NetContinuum Web Application Firewall (NetContinuum/Barracuda Networks)'''
	for item in _[0].items():
		if re.search(r'\ANCI__SessionId\=',item[1] or '',re.I):
			return waf_netcontinuum.__doc__
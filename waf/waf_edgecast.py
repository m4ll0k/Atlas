#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def waf_edgecast(*_):
	'''EdgeCast Web Application Firewall (Verizon)'''
	for item in _[0].items():
		if _[2]==400 and re.search(r'\AECDF',item[1] or '',re.I) is not None:
			return waf_edgecast.__doc__
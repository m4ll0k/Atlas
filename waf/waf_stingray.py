#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def waf_stingray(*_):
	'''Stingray Application Firewall (Riverbed / Brocade)'''
	for item in _[0].items():
		if _[2] in(403,500) and re.search(r'\AX-Mapping-',item[1] or '',re.I):
			return waf_stingray.__doc__
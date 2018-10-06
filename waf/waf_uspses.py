#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def waf_uspses(*_):
	'''USP Secure Entry Server (United Security Providers)'''
	for item in _[0].items():
		if re.search(r'Secure Entry Server',item[1] or '',re.I):
			return waf_uspses.__doc__
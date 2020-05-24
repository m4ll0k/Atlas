#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def waf_naxsi(*_):
	'''NAXSI (NBS System)'''
	for item in _[0].items():
		if re.search('naxsi/waf',item[1] or '',re.I):
			return waf_naxsi.__doc__
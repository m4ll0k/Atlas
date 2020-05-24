#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def waf_radware(*_):
	'''AppWall (Radware)'''
	for item in _[0].items():
		if item[1] == 'x-sl-compstate':
			return waf_radware.__doc__
	if re.search(r'Unauthorized Activity Has Been Detected.+Case Number:',str(_[1]) or '',re.I):
		return waf_radware.__doc__
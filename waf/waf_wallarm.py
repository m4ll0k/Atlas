#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def waf_wallarm(*_):
	'''Wallarm Web Application Firewall (Wallarm)'''
	for item in _[0].items():
		if re.search(r'nginx-wallarm',item[1] or '',re.I):
			return waf_wallarm.__doc__
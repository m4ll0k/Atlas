#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re 

def waf_ciscoacexml(*_):
	'''Cisco ACE XML Gateway (Cisco Systems)'''
	is_true=False
	for item in _[0].items():
		is_true=re.search('ACE XML Gateway',item[1] or '',re.I)is not None
		if is_true: return waf_ciscoacexml.__doc__
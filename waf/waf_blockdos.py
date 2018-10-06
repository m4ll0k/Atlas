#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re 

def waf_blockdos(*_):
	'''BlockDos'''
	is_true=False
	for item in _[0].items():
		is_true=re.search(r'BlockDos\.net',item[1] or '', re.I) is not None
		if is_true:return waf_blockdos.__doc__
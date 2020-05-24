#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re 

def waf_dosarrest(*_):
	'''DOSarrest (DOSarrest Internet Security)'''
	is_true=False
	for item in _[0].items():
		is_true = re.search('DOSarrest',item[1] or "", re.I) is not None
		is_true |= item[0] == 'x-dis-request-id' or False
		if is_true: return waf_dosarrest.__doc__
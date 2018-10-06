#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def waf_sonicwall(*_):
	'''SonicWALL (Dell)'''
	is_true=False
	for item in _[0].items():
		is_true = re.search(r'SonicWALL',item[1] or '',re.I) is not None
		if is_true:return waf_sonicwall.__doc__
	is_true |= re.search(r'This request is blocked by the SonicWALL',_[1],re.I) is not None
	is_true |= re.search(r'Web Site Blocked.+\bnsa_banner',_[1] or '',re.I) is not None
	is_true |= all(_ in (_[1] or '')for _ in ('#shd','#nsa_banner'))
	if is_true: return waf_sonicwall.__doc__

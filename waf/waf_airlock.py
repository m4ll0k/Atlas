#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def waf_airlock(*_):
	'''Airloc (Phion/Ergon)'''
	is_true=False
	for item in _[0].items():
		is_true=re.search(r'\A[_-]?(SESS|LB)=',item[1] or "", re.I) is not None
		if is_true:return waf_airlock.__doc__ 
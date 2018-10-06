#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def waf_bigip(*_):
	'''BIG-IP Application Security Manager (F5 Networks)'''
	is_true=False
	for item in _[0].items():
		is_true  = item[1] == 'close' if item[0] == 'x-cnection' else ''
		is_true  = True if item[0] == 'x-wa-info' else False
		is_true |= re.search(r'\ATS\w{4,}=',item[1] or '',re.I) is not None
		is_true |= re.search(r'BigIP|BIGipServer',item[1] or '',re.I) is not None
		is_true |= re.search(r'\AF5\Z',item[1] or '',re.I) is not None
		is_true &= _[2]>=400
		if is_true:return waf_bigip.__doc__
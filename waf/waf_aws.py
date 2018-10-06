#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def waf_aws(*_):
	'''Amazon Web Services Web Application Firewall (Amazon)'''
	is_true=False
	for item in _[0].items():
		is_true=_[2]==403 and re.search(r'\bAWS',item[1] or '',re.I) is not None
		if is_true:return waf_aws.__doc__
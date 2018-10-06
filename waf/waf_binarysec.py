#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re 

def waf_binarysec(*_):
	'''BinarySEC Web Application Firewall (BinarySEC)'''
	is_true=False
	for item in _[0].items():
		is_true=item[0] in ('x-binarysec-via','x-binarysec-nocache')
		is_true|=re.search('binarysec',item[1] or '',re.I)is not None
		if is_true:return waf_binarysec.__doc__
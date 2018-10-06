#!/usr/bin/env python
# -*- coding:utf-8 -*-

def waf_proventia(*_):
	'''Proventia Web Application Security (IBM)'''
	for item in _[0].items():
		if item[0]=='location' and '/Admin_Files/' in item[1]:
			return waf_proventia.__doc__
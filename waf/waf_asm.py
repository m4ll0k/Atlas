#!/usr/bin/env python
# -*- coding:utf-8 -*-

def waf_asm(*_):
	'''Application Security Manager (F5 Networks)'''
	if 'The requested URL was rejected. Please consult with your administrator.' in _[1]:
		return waf_asm.__doc__
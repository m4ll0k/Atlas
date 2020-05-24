#!/usr/bin/env python
# -*- coding:utf-8 -*-

def waf_armor(*_):
	'''Armor Protection (Armor Defense)'''
	if 'This request has been blocked by website protection from Armor'in _[1]:
		return waf_armor.__doc__
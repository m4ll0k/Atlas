#!/usr/bin/env python
# -*- coding:utf-8 -*-

def waf_isaserver(*_):
	'''ISA Server (Microsoft)'''
	if 'The server denied the specified Uniform Resource Locator (URL). Contact the server administrator.' in _[1]:
		return waf_isaserver.__doc__
	if 'The ISA Server denied the specified Uniform Resource Locator (URL)' in _[1]:
		return waf_isaserver.__doc__
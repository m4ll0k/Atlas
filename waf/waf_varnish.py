#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def waf_varnish(*_):
	'''Varnish FireWall (OWASP)'''
	for item in _[0].items():
		if item[0] == 'x-varnish': return waf_varnish.__doc__
		if re.search(r'varnish\Z|varnish',item[1] or '',re.I):
			return waf_varnish.__doc__
	if _[2] in (400,404) and re.search(r'\bXID: \d+',_[1] 
		or '') or 'Request rejected by xVarnish-WAF' in _[1]: return waf_varnish.__doc__
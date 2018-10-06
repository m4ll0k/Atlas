#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def waf_sucuri(*_):
	'''CloudProxy WebSite Firewall (Sucuri)'''
	for item in _[0].items():
		if _[2]==403 and re.search('Sucuri/Cloudproxy',item[1] or '',re.I):
			return waf_sucuri.__doc__
	if re.search('Access Denied - Sucuri Website Firewall|Sucuri WebSite Firewall - CloudProxy - Access Denied',
		_[1] or '', re.I): return waf_sucuri.__doc__
	if re.search(r'Questions\?.+cloudproxy@sucuri\.net',_[1] or '',re.I):
		return waf_sucuri.__doc__
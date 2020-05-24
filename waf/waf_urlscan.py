#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def waf_urlscan(*_):
	'''UrlScan (Microsoft)'''
	for item in _[0].items():
		if re.search(r'Rejected-By-UrlScan',item[1] or '',re.I):
			return waf_urlscan.__doc__
	if _[2]!=200 and re.search(r'\/Rejected-By-UrlScan',str(_[1]) or '',re.I) is not None:
		return waf_urlscan.__doc__
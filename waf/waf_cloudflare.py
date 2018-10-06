#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def waf_cloudflare(*_):
	'''CloudFlare Web Application Firewall (CloudFlare)'''
	is_true=False
	for item in _[0].items():
		is_true=re.search('cloudflare-nginx',item[1] or '', re.I) is not None
		if is_true: return waf_cloudflare.__doc__
		if _[2] >= 400:
			is_true |= re.search(r'\A_cfduid\=',item[1] or '', re.I) is not None
			is_true |= item[1] == 'cf-ray' or False
			is_true |= re.search(r'CloudFlare Ray ID\:|var CloudFlare\=',_[1] or '',re.I) is not None
			if is_true: return waf_cloudflare.__doc__
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def waf_cloudfront(*_):
	'''CloudFront (Amazon)'''
	is_true=False
	for item in _[0].items():
		is_true = re.search(r'cloudfront',item[1] or '',re.I) is not None
		is_true = item[0] == 'x-amz-cf-id' or False	
		if is_true: return waf_cloudfront.__doc__
		
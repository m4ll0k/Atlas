#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def waf_knownsec(*_):
	'''KS-WAF (Knownsec)'''
	if re.search(r"url\('/ks-waf-error\.png'\)", _[1] or '',re.I):
		return waf_knownsec.__doc__
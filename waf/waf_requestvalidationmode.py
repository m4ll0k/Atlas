#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def waf_requestvalidationmode(*_):
	'''ASP.NET RequestValidationMode (Microsoft)'''
	if 'ASP.NET has detected data in the request that is potentially dangerous' in _[1]:
		return waf_requestvalidationmode.__doc__
	if 'Request Validation has detected a potentially dangerous client input value' in _[1]:
		return waf_requestvalidationmode.__doc__
	if 'HttpRequestValidationException' in _[1] and _[2]==500:
		return waf_requestvalidationmode.__doc__
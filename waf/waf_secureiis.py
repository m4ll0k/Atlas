#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def waf_secureiis(*_):
	'''SecureIIS Web Server Security (BeyondTrust)'''
	if re.search(r'SecureIIS[^<]+Web Server Protection',_[1] or '',re.I):
		return waf_secureiis.__doc__
	if re.search(r'http://www.eeye.com/SecureIIS/|\?subject=[^>]*SecureIIS Error',_[1] or '',re.I):
		return waf_secureiis.__doc__
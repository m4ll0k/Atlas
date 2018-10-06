#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def waf_sophos(*_):
	'''UTM Web Protection (Sophos)'''
	if re.search('Powered by UTM Web Protection',_[1] or '',re.I):
		return waf_sophos.__doc__
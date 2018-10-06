#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def waf_kona(*_):
	'''KONA Security Solutions (Akamai Technologies)'''
	for item in _[0].items():
		if re.search(r'AkamaiGHost',item[1] or '', re.I):
			return waf_kona.__doc__
	if _[2] in (400,403,501) and re.search(r'Reference #[0-9a-f.]+',_[1] or '',re.I):
		return waf_kona.__doc__
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def waf_watchguard(*_):
	'''WatchGuard (WatchGuard Technologies)'''
	for item in _[0].items():
		if _[2] >= 400 and re.search(r'\AWatchGuard',item[1] or '',re.I):
			return waf_watchguard.__doc__
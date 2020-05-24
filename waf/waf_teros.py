#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def waf_teros(*_):
	'''Teros/Citrix Application Firewall Enterprise (Teros/Citrix Systems)'''
	for item in _[0].items():
		if re.search(r'\Ast8(id|_wat|_wlf)',item[1] or '',re.I):
			return waf_teros.__doc__
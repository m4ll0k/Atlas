#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def waf_barracuda(*_):
	'''Barracuda Web Application Firewall (Barracuda Networks)'''
	is_true=False
	for item in _[0].items():
		is_true=re.search(r'\Abarra_counter_session=',item[1] or '',re.I) is not None
		is_true|=re.search(r'(\A|\b)barracuda_',item[1] or '',re.I) is not None
		if is_true:return waf_barracuda.__doc__
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def waf_paloalto(*_):
	'''Palo Alto Firewall (Palo Alto Networks)'''
	if re.search('has been blocked in accordance with company policy',_[1] or '',re.I):
		return waf_paloalto.__doc__
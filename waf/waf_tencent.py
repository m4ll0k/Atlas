#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def waf_tencent(*_):
	'''Tencent Cloud Web Application Firewall (Tencent Cloud Computing)'''
	if _[2]==405 and 'waf.tencent-cloud.com' in _[1]:
		return waf_tencent.__doc__
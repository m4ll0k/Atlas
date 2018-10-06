#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def waf_netscaler(*_):
	'''NetScaler (Citrix Systems)'''
	is_true=False
	for item in _[0].items():
		is_true  = re.search(r'\Aclose',item[1] if item[0] in ('Cneonction','nnCoection') else '',re.I)is not None
		is_true |= re.search(r'\A(ns_af=|citrix_ns_id|NSC_)',item[1] or '',re.I)is not None
		is_true |= re.search(r'\Ans-cache',item[1] if item[0]=='via' else '',re.I)is not None
		if is_true: return waf_netscaler.__doc__
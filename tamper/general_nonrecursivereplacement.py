#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re 
import random

def general_nonrecursivereplacement(payload):
	# -- general -- #
	_payload = payload
	keywords = ('UNION','SELECT','INSERT','UPDATE','FROM','WHERE')
	if payload:
		for keyword in keywords:
			_ = random.randint(1,len(keyword)-1)
			_payload = re.sub(r'(?i)\b%s\b'%keyword,'%s%s%s'%(
				keyword[:_],keyword,keyword[_:]),_payload)
	return _payload
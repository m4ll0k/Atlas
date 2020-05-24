#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import re
from lib.file import *

path = os.path.join(
	os.path.join(os.path.abspath('.'),'db'),
	'statements.txt'
)

def general_uppercase(payload):
	# -- general -- 
	statements = readfile(path)
	_payload = payload
	if payload:
		for match in re.finditer(r'[A-Za-z_]+',_payload):
			word = match.group()
			if word.upper() in statements:
				_payload = _payload.replace(word,word.upper())
	return _payload
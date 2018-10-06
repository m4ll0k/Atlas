#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import re
from lib.file import *

path = os.path.join(
	os.path.join(os.path.abspath('.'),'db'),
	'statements.txt')

def general_lowercase(payload):
	# -- general -- #
	_payload = payload
	statements = readfile(path)
	if payload:
		for match in re.finditer(r'\b[A-Za-z]+\b',_payload):
			word = match.group()
			if word.upper() in statements:
				_payload = _payload.replace(word, word.lower())
	return _payload
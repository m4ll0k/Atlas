#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import re
import random
from lib.file import *

path = os.path.join(
	os.path.join(os.path.abspath('.'),'db'),
	'statements.txt'
	)

def general_randomcase(payload):
	# -- general -- #
	statements = readfile(path)
	_payload = payload 
	if payload:
		for match in re.finditer(r'\b[A-Za-z_]+\b',_payload):
			word = match.group()
			if word.upper() in statements:
				m_word = random.choice(word)
				if m_word: 
					_payload = _payload.replace(m_word,m_word.lower())
	return _payload
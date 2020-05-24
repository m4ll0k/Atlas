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

def general_randomcomments(payload):
	# -- general -- #
	statements = readfile(path)
	_payload = payload 
	if payload:
		for match in re.finditer(r'\b[A-Za-z_]+\b',payload):
			word = match.group()
			if word.upper() in statements:
				m_word = word[random.randint(0,len(word))-1]
				if m_word:
					_payload = _payload.replace(m_word,m_word+'/**/')
	return _payload
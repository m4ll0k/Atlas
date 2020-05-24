#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import re
from lib.file import *

path = os.path.join(
	os.path.join(os.path.abspath('.'),'db'),
	'statements.txt'
)

def mysql_versionedkeywords(payload):
	# -- general -- 
	statements = readfile(path)
	_payload = payload

	def process(match):
		word = match.group('word')
		if word.upper() in statements:
			return match.group().replace(word,'/*!%s*/'%(word))
		else:
			return match.group()
	if payload:
		_payload = re.sub(r"(?<=\W)(?P<word>[A-Za-z_]+)(?=[^\w(]|\Z)",lambda match: process(match),_payload)
		_payload = _payload.replace(' /*!','/*!').replace('*/ ','*/')
	return _payload
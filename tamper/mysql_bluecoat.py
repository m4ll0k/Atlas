#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import re
from lib.file import *

path = os.path.join(
	os.path.join(os.path.abspath('.'),'db'),
	'statements.txt')

def mysql_bluecoat(payload):
	# -- mysql -- #
	_payload = payload
	statements = readfile(path)
	def process(match):
		word = match.group('word')
		if word.upper() in statements:
			return match.group().replace(word,'%s%%09'%word)
		else:
			return match.group()
	if payload:
		_payload = re.sub(r'\b(?P<word>[A-Z_]+)(?=[^\w(]|\Z)',
			lambda match:process(match),_payload) 
		_payload = re.sub(r'\s*=\s*',' LIKE ',_payload)
		_payload = _payload.replace('%09 ','%09')

	return _payload
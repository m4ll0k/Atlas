#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import re
from lib.file import *

path = os.path.join(
	os.path.join(os.path.abspath('.'),'db'),
	'statements.txt')

def mysql_halfversionedmorekeywords(payload):
	# -- mysql -- #
	statements = readfile(path)
	def process(p):
		_p = p 
		for statement in statements:
			statement = str(statement)
			if statement in p:
				match = re.findall('\s*%s\s*'%statement,_p)[0]
				_p = re.sub(match,match.replace(' ','/*!0'),_p)
		return _p
	_payload = process(payload)
	return _payload
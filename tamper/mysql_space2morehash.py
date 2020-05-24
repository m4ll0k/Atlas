#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import re
import random
import string
from lib.file import *

path = os.path.join(
	os.path.join(os.path.abspath('.'),'db'),
	'statements.txt'
)

def mysql_space2morehash(payload):
	# -- mysql -- #
	_payload = ""
	statements = readfile(path)
	# --
	def process(match):
		word = match.group('word')
		randomStr = ''.join(random.choice(
			string.ascii_uppercase + string.ascii_lowercase) for _ in range(random.randint(5,12)))
		if word.upper() in statements:
			return match.group().replace(word,"%s%%23%s%%0A"%(word,randomStr))
		else:
			return match.group()
	if payload:
		payload = re.sub(r'(?<=\W)(?P<word>[A-Za-z_]+)(?=\W|\Z)',lambda match:process(match),payload)
		for i in range(len(payload)):
			if payload[i].isspace():
				randomStr = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase)
					for _ in range(random.randint(6,12)))
				_payload += '%%23%s%%0A'%randomStr
			elif payload[i] == '#' or payload[i:i+3] == '-- ':
				_payload += payload[i:]
				break
			else:
				_payload += payload[i]
	return _payload
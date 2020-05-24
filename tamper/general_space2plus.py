#!/usr/bin/env python
# -*- coding:utf-8 -*-

def general_space2plus(payload):
	# -- general -- #
	_payload = payload
	if payload:
		_payload = ""
		quote,doublequote,firstspace = False,False,False
		for i in range(len(payload)):
			if not firstspace:
				if payload[i].isspace():
					firstspace = True
					_payload += "+"
					continue
			elif payload[i] == '\'':
				quote = not quote
			elif payload[i] == '"':
				doublequote = not doublequote
			elif payload[i] == " " and not doublequote and not quote:
				_payload += "+"
				continue
			_payload += payload[i]
	return _payload
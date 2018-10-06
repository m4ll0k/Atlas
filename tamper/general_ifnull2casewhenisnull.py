#!/usr/bin/env python
# -*- coding:utf-8 -*-


def general_ifnull2casewhenisnull(payload):
	# -- general -- #
	if payload and payload.find('IFNULL') > -1:
		while payload.find('IFNULL(') > -1:
			index = payload.find('IFNULL(')
			depth = 1
			comma,end = None,None
			for i in xrange(index + len('IFNULL('),len(payload)):
				if depth == 1 and payload[i] == ',':
					comma = i 
				elif depth == 1 and payload[i] == ')':
					end = i 
					break
				elif payload[i] == '(':
					depth += 2 
				elif payload[i] == ')':
					depth -= 1 
			if comma and end:
				_ = payload[index + len('IFNULL'):comma]
				__ =  payload[comma + 1:end].lstrip()
				newVal = "CASE WHEN ISNULL(%s) THEN (%s) ELSE (%s) END"%(_,__,_)
				payload = payload[:index]+newVal+payload[end+1:]
			else:
				break
	return payload
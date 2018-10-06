#!/usr/bin/env python
# -*- coding:utf-8 -*-

def mysql_concat2concatws(payload):
	# -- mysql -- #
	if payload:
		payload = payload.replace('CONCAT(','CONCAT_WS(MID(CHAR(0),0,0),')
	return payload
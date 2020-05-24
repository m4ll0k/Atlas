#!/usr/bin/env python
# -*- coding:utf-8 -*-

def mysql_space2morecomment(payload):
	# -- mysql -- # 
	return payload.replace(' ','/**_**/') if payload else payload

#!/usr/bin/env python
# -*- coding:utf-8 -*-

def general_unionalltounion(payload):
	# -- general -- #
	return payload.replace('UNION ALL SELECT','UNION SELECT') if payload else payload
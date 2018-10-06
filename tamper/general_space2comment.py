#!/usr/bin/env python
# -*- coding:utf-8 -*-

def general_space2comment(payload):
	# -- general -- #
	return payload.replace(' ','/**/') if payload else payload
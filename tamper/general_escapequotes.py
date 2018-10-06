#!/usr/bin/env python
# -*- coding:utf-8 -*-

def general_escapequotes(payload):
	# -- general -- # 
	return payload.replace("'","\\'").replace('"','\\"')
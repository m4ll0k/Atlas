#!/usr/bin/env python
# -*- coding:utf-8 -*-

def mssql_appendnullbyte(payload):
	# -- mssql -- #
	return "%s%%00"%payload if payload else payload
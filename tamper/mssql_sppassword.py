#!/usr/bin/env python
# -*- coding:utf-8 -*-

def mssql_sppassword(payload):
	# -- mssql -- #
	_payload = ""
	if payload:
		_payload = "%s%ssp_password"%(payload,
			'--' if not any(_ if _ in payload else None for _ in ('#','-- ')) else "")
	return _payload
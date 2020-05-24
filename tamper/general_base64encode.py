#!/usr/bin/env python
# -*- coding:utf-8 -*-

import base64

def general_base64encode(payload):
	# -- generic -- #
	return base64.b64encode(payload.encode('utf-8')) if payload else payload
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def general_htmlencode(payload):
	# -- general -- #
	return re.sub(r"[^\w]",lambda match: "&#%d;"%ord(match.group(0)),payload) if payload else payload
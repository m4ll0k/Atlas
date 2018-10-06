#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def waf_senginx(*_):
	'''SEnginx (Neusoft Corporation)'''
	if re.search('SENGINX-ROBOT-MITIGATION',_[1] or '',re.I):
		return waf_senginx.__doc__
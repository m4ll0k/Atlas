#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def waf_trafficshield(*_):
	'''TrafficShield (F5 Networks)'''
	for item in _[0].items():
		if re.search(r'F5-TrafficShield|\AASINFO\=',item[1] or '',re.I):
			return waf_trafficshield.__doc__
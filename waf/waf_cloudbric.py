#!/usr/bin/env python
# -*- coding:utf-8 -*-

def waf_cloudbric(*_):
	'''Cloudbric Web Application Firewall (Cloudbric)'''
	if _[2]>=400 and all(_ in (_[1] or '') for _ in ('Cloudbric','Malicious Code Detected')):
		return waf_cloudbric.__doc__
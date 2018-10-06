#!/usr/bin/env python
# -*- coding:utf-8 -*-

def waf_sitelock(*_):
	'''TrueShield Web Application Firewall (SiteLock)'''
	is_true=False
	is_true=any(_ in (_[1] or "") for _ in ("SiteLock Incident ID", "sitelock-site-verification", "sitelock_shield_logo"))
	if is_true:return waf_sitelock.__doc__
#!/usr/bin/env python
# -*- coding:utf-8 -*-

def general_apostrophenullencode(payload):
	# -- generic -- #
	return payload.replace('\'',"%00%27") if payload else payload
#!/usr/bin/env python
# -*- coding:utf-8 -*-

def general_apostrophemask(payload):
	# -- generic -- #
	return payload.replace('\'',"%EF%BC%87") if payload else payload
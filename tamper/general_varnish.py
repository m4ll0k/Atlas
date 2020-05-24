#!/usr/bin/env python
# -*- coding:utf-8 -*-


def general_varnish(payload):
	# -- general -- 
    # https://github.com/sqlmapproject/sqlmap/blob/master/tamper/varnish.py
    # add header `X-originating-IP: 127.0.0.1` manually 
    return payload
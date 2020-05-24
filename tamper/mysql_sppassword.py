#!/usr/bin/env python
# -*- coding:utf-8 -*-

def mysql_sppassword(payload):
    # -- mysql 
    _payload = ""

    if payload:
        _payload = "%s%ssp_password"%(payload,'-- ' if not any(_ if _ in payload else None for _ in ('#',"-- ")) else "")
    return _payload
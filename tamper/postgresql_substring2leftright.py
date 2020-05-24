#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def postgresql_substring2leftright(payload):
    # postgresql
    _payload = payload
    if payload:
        match = re.search(r"SUBSTRING\((.+?)\s+FROM[^)]+(\d+)[^)]+FOR[^)]+1\)", payload)
        if match:
            pos = int(match.group(2))
            if pos == 1:
                _ = "LEFT(%s,1)"%(match.group(1))
            else:
                _ = "LEFT(RIGTH(%s,%d),1)"%(match.group(1),1-pos)
            _payload = _payload.replace(match.group(0),_)
    return _payload
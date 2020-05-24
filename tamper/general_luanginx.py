#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random
import string 

delimiter = '&'

def general_luanginx(payload):
	# -- generic 
    _payload = payload
    if payload:
        _payload = delimiter.join('%s='%"".join(random.sample(string.ascii_letters+string.digits,2)) for _ in range(500)) +payload
    return _payload

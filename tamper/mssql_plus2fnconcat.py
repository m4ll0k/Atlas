#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

# https://github.com/sqlmapproject/sqlmap/blob/master/lib/core/common.py#L5022
def zeroDepthSearch(expression, value):
    retVal = []

    depth = 0
    for index in range(len(expression)):
        if expression[index] == '(':
            depth += 1
        elif expression[index] == ')':
            depth -= 1
        elif depth == 0:
            if value.startswith('[') and value.endswith(']'):
                if re.search(value, expression[index:index + 1]):
                    retVal.append(index)
            elif expression[index:index + len(value)] == value:
                retVal.append(index)

    return retVal


def mssql_plus2fnconcat(payload):
    _payload = payload
    if payload:
        match = re.search(r"('[^']+'|CHAR\(\d+\))\+.*(?<=\+)('[^']+'|CHAR\(\d+\))",_payload)
        if match:
            old = match.group(0)
            parts = []
            last = 0
            for index in zeroDepthSearch(old,'+'):
                parts.append(old[last:index].strip('+'))
                last = index 
            parts.append(old[last:].strip('+'))
            replacement = parts[0]
            for i in range(1,len(parts)):
                replacement = "{fn CONCAT(%s,%s)}"%(replacement,parts[i])
            _payload  = _payload.replace(old,replacement)
    return _payload


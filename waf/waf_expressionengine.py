#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def waf_expressionengine(*_):
	'''ExpressionEngine (EllisLab)'''
	if 'Invalid GET Data' in _[1]: return waf_expressionengine.__doc__
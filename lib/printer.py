#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import time 

r = '\033[%s;31m'
g = '\033[%s;32m'
y = '\033[%s;33m'
b = '\033[%s;34m'
c = '\033[%s;35m'
w = '\033[%s;38m'
e = '\033[0m'

strftime = time.strftime("%H:%M:%S")

def plus(string,_=False):
	if string:
		print("[%s%s%s] [%sINFO%s] %s%s%s"%(
			c%1,strftime,e,g%0,e,g%1,string,e)
		)
		if(_):sys.exit(0)

def plus2(string,_=False):
	if string:
		print("[%s%s%s] [%sINFO%s] %s%s%s"%(
			c%1,strftime,e,g%1,e,g%0,string,e)
		)
		if(_):sys.exit(0)

def warn(string,_=False):
	if string:
		print("[%s%s%s] [%sWARN%s] %s%s%s"%(
			c%1,strftime,e,r%0,e,r%1,string,e)
		)
		if(_):sys.exit(0)

def warn2(string,_=False):
	if string:
		print("[%s%s%s] [%sWARN%s] %s%s%s"%(
			c%1,strftime,e,r%1,e,y%0,string,e)
		)
		if(_):sys.exit(0)

def info(string,_=False):
	if string:
		print("[%s%s%s] [%sINFO%s] %s%s%s"%(
			c%1,strftime,e,y%0,e,y%1,string,e)
		)
		if(_):sys.exit(0)

def info2(string,_=False):
	if string:
		print("[%s%s%s] [%sINFO%s] %s%s%s"%(
			c%1,strftime,e,y%1,e,y%0,string,e)
		)
		if(_):sys.exit(0)


def payload(string,_=False):
	if string:
		print("[%s%s%s] [%sPAYLOAD%s] %s%s%s"%(
			c%1,strftime,e,b%1,e,w%1,string,e)
		)
		if(_):sys.exit(0)
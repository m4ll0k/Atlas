#!/usr/bin/env python
# -*- coding:utf-8 -*-

def readfile(path):
	if(path):
		return [file.strip() for file in open(path,'rb')]
	return
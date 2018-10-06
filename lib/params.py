#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

class Params:
	def __init__(self,url,payload,data):
		self.url = url
		self.data = data
		self._params = []
		self.payload = payload
	
	def get(self):
		params = self.url.split('?')[1].split('&')
		for param in params:
			ppayload = param.replace(param.split('=')[1],self.payload)
			porignal = param.replace(ppayload.split('=')[1],param.split('=')[1])
			self._params.append(re.sub(porignal,ppayload,self.url))

	def post(self):
		params = self.data.split('&')
		for param in params:
			ppayload = param.replace(param.split('=')[1],self.payload)
			porignal = param.replace(ppayload.split('=')[1],param.split('=')[1])
			self._params.append(self.data.replace(porignal,ppayload))

	def run(self):
		if '=' in self.url and self.data == None:self.get()
		elif '=' not in self.url and '=' in self.data:self.post()
		elif '=' in self.url and '=' in self.data:self.get();self.post()
		return self._params
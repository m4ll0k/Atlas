#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
from urllib.parse import *

class Params(object):
	def __init__(self,url: str,payload:str,data: str,headers: dict) -> None:
		self.url = url
		self.data = data
		self.headers = headers
		self._params = {
				'get'        : [],
				'post'       : [],
				'headers'    : {},
				'h_injected' : False
			}
		self.payload = payload
	
	def get(self) -> None:
		if re.search(r'%%.*?%%',self.url,re.I):
			temp_url = re.sub(r'%%.*?%%',self.payload,self.url)
			self._params['get'].append(temp_url)
		elif '?' in self.url and '=' in self.url:
			params = self.url.split('?')[1].split('&')
			for param in params:
				ppayload = param.replace(param.split('=')[1],self.payload)
				porignal = param.replace(ppayload.split('=')[1],param.split('=')[1])
				# replace and append in params list
				self._params['get'].append(re.sub(porignal,ppayload,self.url))

		# --

	def post(self) -> None:
		if re.search(r'%%.*?%%',self.data,re.I):
			temp_data = re.sub(r'%%.*?%%',self.payload,self.data)
			self._params['post'].append(temp_data)
		elif '=' in self.data:
			params = self.data.split('&')
			for param in params:
				ppayload = param.replace(param.split('=')[1],self.payload)
				porignal = param.replace(ppayload.split('=')[1],param.split('=')[1])
				self._params['post'].append(self.data.replace(porignal,ppayload))
		# --
	def _headers(self) -> None:
		for i in self.headers.items():
			if (re.search(r'%%.*?%%',i[0],re.I)):
				h1 = re.sub(r'%%.*?%%',self.payload,i[0])
				h2 = i[1]
				self.headers.pop(i[0])
				self.headers[h1] = h2 
				self._params['h_injected'] = True
			elif (re.search(r'%%.*?%%',i[1],re.I)):
				h2 = re.sub(r'%%.*?%%',self.payload,i[1])
				self.headers[i[0]] = h2 
				self._params['h_injected'] = True
		self._params['headers'].update(self.headers)

	def inject(self) -> list:
		self.get()
		self.post()
		self._headers()
		return self._params

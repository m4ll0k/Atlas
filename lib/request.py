#!/usr/bin/env python
# -*- coding:utf-8 -*-

import ssl
import socket
import urllib2

if hasattr(ssl,'_create_unverified_context'):
	ssl._create_unverified_context = ssl._create_unverified_context

class Request(object):
	# -- request -- #
	def __init__(self,*kwargs):
		self.kwargs = kwargs[0]

	def send(self,url,method='GET',data=None):
		agent    = self.kwargs['agent']
		proxy    = self.kwargs['proxy']
		cookie   = self.kwargs['cookie']
		timeout  = self.kwargs['timeout']
		redirect = self.kwargs['allow-redirect']
		# -- process -- # 
		if method:method = method.upper()
		if data is None: data = {}
		# -- add headers -- #
		headers = {}
		headers['User-Agent'] = agent
		if cookie:headers['Cookie'] = cookie
		# -- socket timeout -- #
		if timeout:socket.setdefaulttimeout(timeout)
		# -- handled http and https -- #
		handlers = [urllib2.HTTPHandler(),urllib2.HTTPSHandler()]
		# -- process redirect -- #
		if redirect is False:handlers.append(NoRedirectHandler)
		# -- process proxies -- # 
		if proxy:
			handlers.append(urllib2.ProxyHandler({
				'http' : proxy,
				'https': proxy
				})
			)
		# -- install opener -- #
		opener = urllib2.build_opener(*handlers)
		urllib2.install_opener(opener)
		# -- process request -- #
		if method.lower() == "get":
			if data: url = get_params(url,data)
			req = urllib2.Request(url,headers=headers)
		elif method.lower() == "post":
			req = urllib2.Request(url,data=data,headers=headers)
		# -- urlopen -- #
		try:
			resp = urllib2.urlopen(req)
		except urllib2.HTTPError,e:
			resp = e 
		return Resp(resp)

class NoRedirectHandler(urllib2.HTTPRedirectHandler):
	def http_error_302(self,req,fp,code,msg,headers):
		pass
	http_error_302 = http_error_302 = http_error_302 = http_error_302

class Resp(object):
	def __init__(self,resp):
		self.url = resp.geturl()
		self.code  = resp.getcode()
		self.content = resp.read()
		self.headers = resp.headers.dict

def get_params(url,data):
	if url.endswith('?'):return url + data
	if not url.endswith('?'):return url+'?'+data
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import ssl
import random
import socket
from urllib import request as urllib2

if hasattr(ssl,'_create_unverified_context'):
	ssl._create_unverified_context = ssl._create_unverified_context


class Request(object):
	# -- request -- #
	def __init__(self,*kwargs):
		self.kwargs = kwargs[0]

	def send(self,url,method='GET',data=None,headers={}):
		agent    = self.kwargs['agent']
		proxy    = self.kwargs['proxy']
		cookie   = self.kwargs['cookie']
		timeout  = self.kwargs['timeout']
		headers_ = self.kwargs['headers'] if self.kwargs['headers'] == headers else headers
		redirect = self.kwargs['allow-redirect']
		# -- process -- # 
		if method:method = method.upper()
		if data is None: data = {}
		# -- disable ssl check -- *
		ctx = ssl.create_default_context()                                                                      
		ctx.check_hostname = False                                                                              
		ctx.verify_mode = ssl.CERT_NONE
		# -- add headers -- #
		headers = {}
		headers['User-Agent'] = agent
		for header in headers_.items():
			headers[header[0]] = header[1]
		# -- //
		if cookie:headers['Cookie'] = cookie
		# -- socket timeout -- #
		if timeout:socket.setdefaulttimeout(timeout)
		# -- handled http and https -- #
		handlers = [urllib2.HTTPHandler(),urllib2.HTTPSHandler(context=ctx)]
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
		except urllib2.HTTPError as e:
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
		self.headers = {}
		for header in resp.getheaders():
			self.headers[header[0].lower()] = header[1]

def get_params(url,data):
	if url.endswith('?'):return url + data
	if not url.endswith('?'):return url+'?'+data

def randomIp():
	octets = []
	while not octets or octets[0] in (10, 172, 192):
		octets = random.sample(range(1, 255), 4)
	return '.'.join(str(_) for _ in octets)

# https://github.com/sqlmapproject/sqlmap/blob/master/tamper/xforwardedfor.py
def xforwardedfor():
	return {
		'X-Forwarded-For' : randomIp(),
		'X-Client-Ip'     : randomIp(),
		'X-Real-Ip'       : randomIp(),
		'CF-Connecting-IP': randomIp(),
		'True-Client-IP'  : randomIp(),
		'Via'             : '1.1 Chrome-Compression-Proxy',
		'CF-IPCountry'    :  random.sample(('GB', 'US', 'FR', 'AU', 'CA', 'NZ', 'BE', 'DK', 'FI', 'IE', 'AT', 'IT', 'LU', 'NL', 'NO', 'PT', 'SE', 'ES', 'CH'), 1)[0]
	}
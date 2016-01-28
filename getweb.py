#!/usr/bin/env python
# -*- coding:utf-8 -*-
#coder:qiaoy<TraceurQ@gmail.com>

'''
多线程获取Web信息，title和body
'''

import threading, Queue, time
import sys, requests
import MySQLdb
from BeautifulSoup import *

try:
	conn = MySQLdb.connect(host='localhost',user='root',passwd='',db='test',charset='utf8')
	cursor = conn.cursor()
except Exception, e:
	print e
	sys.exit()

#headers = {'Accept-Language': 'zh-cn','Content-Type': 'application/x-www-form-urlencoded','User-Agent': 'Mozilla/4.0 (compatible MSIE 6.00 Windows NT 5.1 SV1)',}
FILE_LOCK = threading.Lock()
SHARE_Q = Queue.Queue()  #构造一个不限制大小的的队列
_WORKER_THREAD_NUM = 100  #设置线程的个数

class MyThread(threading.Thread) :

	def __init__(self, func) :
		super(MyThread, self).__init__()  #调用父类的构造函数
		self.func = func  #传入线程函数逻辑

	def run(self) :
		self.func()

def worker() :
	global SHARE_Q
	while not SHARE_Q.empty():
		url = SHARE_Q.get() #获得任务
		getwebvalue(url)
		time.sleep(1)
		SHARE_Q.task_done()
		
def getwebvalue(url):
	s_ip = url
	try:
	#	res = requests.get(s_ip, headers = headers,timeout=5,allow_redirects=False)
		res = requests.get(s_ip,timeout=5,allow_redirects=False)
		res.encoding =  res.apparent_encoding
		if res.status_code == 200 and res.text != '':
			html = BeautifulSoup(res.text)
			try:
				server = res.headers['server'].replace('\"','\'')
			except:
				server=''
			try:
				title = html.title.text.replace('\"','\'')
			except:
				title = ''
			try:
				body = html.body.text.replace('\"','\'').replace('\n',' ')
			except:
				body = ''
			sql = "INSERT INTO web(`ip`, `server`, `title`, `body`) VALUES (%s, %s, %s, %s)"
#			print sql
			cursor.execute(sql,(s_ip.replace('http://',''),server,title,body))
#			print "\"%s\"	\"%s\"	\"%s\"	\"%s\""%(s_ip.replace('http://',''),server,title,body)
	except:pass

def main() :
	global SHARE_Q
	threads = []
	#向队列中放入任务, 真正使用时, 应该设置为可持续的放入任务
	for i in open('ip.txt','r') :   
		SHARE_Q.put('http://%s'%i.replace('\n',''))
	for i in xrange(_WORKER_THREAD_NUM) :
		thread = MyThread(worker)
		thread.start()  #线程开始处理任务
		threads.append(thread)
	for thread in threads :
		thread.join()
	SHARE_Q.join()
	print "Spider Successful!!!"

if __name__ == '__main__':
	main()

#!/usr/bin/env python
# coding: UTF-8
# A mini webserver for get HTTP methods GET, POST
# Coder:qiaoy<qiaoy.py@gmail.com>

'''

旁挂流量，可引导流量到mini webserver端口上，根据需求定制格式，做数据分析。
['time','sip','dip','method','uri','referer','data'] = [请求时间,来源IP,目标地址,请求方式,访问路径,请求来源,参数与内容]

'''

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from optparse import OptionParser
from urlparse import urlparse
import csv,time,cgi

class RequestHandler(BaseHTTPRequestHandler):

    
    def do_GET(self):
        
        request_path = self.path

	#file_headers = ['time','sip','dip','method','uri','referer','data']
	file_itmes = []

	itime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

	try:
		# WAF will put the SIP in headers by : 'bc4ba334-fe56-42f4-b8db-4cdf738e52bc'
		sip = self.headers['bc4ba334-fe56-42f4-b8db-4cdf738e52bc'].split(':')[0]
	except:
		sip=''

	try:
		dip = self.headers['host']
	except:
		dip=''

	method = 'GET'

	uri = urlparse(self.path).path

	try:
		referer = self.headers['referer']
	except:
		referer = ''

	data = urlparse(self.path).query

	file_itmes = [itime,sip,dip,method,uri,referer,data]

	with open("access_log.csv", "a") as f:
	    writer = csv.writer(f,quotechar = "\"")
	    writer.writerow(file_itmes)

#        self.send_response(200)

        
    def do_POST(self):
        
        request_path = self.path
	file_itmes = []

	itime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

	try:
		# WAF will put the SIP in headers by : 'bc4ba334-fe56-42f4-b8db-4cdf738e52bc'
		sip = self.headers['bc4ba334-fe56-42f4-b8db-4cdf738e52bc'].split(':')[0]
	except:
		sip=''

	try:
		dip = self.headers['host']
	except:
		dip=''

	method = 'POST'

	uri = urlparse(self.path).path

	try:
		referer = self.headers['referer']
	except:
		referer = ''

        content_length = self.headers.getheaders('content-length')
        length = int(content_length[0]) if content_length else 0
        
        data = self.rfile.read(length)

	file_itmes = [itime,sip,dip,method,uri,referer,data]

	with open("access_log.csv", "a") as f:
	    writer = csv.writer(f,quotechar = "\"")
	    writer.writerow(file_itmes)

#        self.send_response(200)

        
def main():
    port = 80
    print('Listening on localhost:%s' % port)
    server = HTTPServer(('', port), RequestHandler)
    server.serve_forever()

        
if __name__ == "__main__":
    parser = OptionParser()
    parser.usage = ("Creates an http-server that will echo out any GET or POST parameters\n"
                    "Run:\n\n"
                    "   reflect")
    (options, args) = parser.parse_args()
    
    main()

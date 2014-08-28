#!/usr/bin/python
# coding: UTF-8
#coder:qiaoy<TraceurQ@gmail.com>
'''
本地社工库
'''

import os,sys,datetime

def usage():
	print 'python sgk.py value'
	
def logo():
	print ' --------------------------------'
	print '|-------Local Big Data-----------|'
	print ' --------------------------------'


def find(value,ku):
	for i in open(ku,'r'):
		if value in i:
			print 'Find some string in '+ku+':'
			print i

			
if __name__ == "__main__":
	if len(sys.argv) <=1:
		usage()
	logo()
	value = sys.argv[1]
	starttime = datetime.datetime.now()
	for i in os.listdir('.'):
		if '.txt' in i:
			find(value,i)
	endtime = datetime.datetime.now()
	print 'Use time:	'+str((endtime - starttime).seconds)+'	S'

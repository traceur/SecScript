#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#Code : Qiaoy<TraceurQ@gmail.com>

'''
mysql 社工库查询脚本
'''

import MySQLdb,sys,datetime
import sys,os

reload(sys)
sys.setdefaultencoding("utf-8")

try:
    conn = MySQLdb.connect(host='localhost',user='root',passwd='',charset='utf8')
except Exception, e:
    print e
    sys.exit()

	
def usage():
	print ' '+'='*80
	print '|'
	print '|'
	print '|	python sgk.py [name/email/QQNum/realname/tel/ctfid/passwd] [like/equal] value'
	print '|'
	print '|'
	print ' '+'='*80
	
	
def search(mark,value,like):
	starttime = datetime.datetime.now()
	cursor = conn.cursor()
	list_table = 'select table_name from information_schema.tables where table_name like \'shegong%\';'
	cursor.execute(list_table)
	sql_tables = cursor.fetchall()
	for i in sql_tables:
		if 'shegong_qun_group' in i[0]:
			search_sql = 'select * from qun.'+i[0]+' where '+mark+'='+value+';'
		elif 'shegong_qun_qunlist' in i[0]:
			pass
		else:
			if like == 'like':
				search_sql = 'select * from shegong.'+i[0]+' where '+mark+' like \'%'+value+'%\';'
			elif like == 'equal':
				search_sql = 'select * from shegong.'+i[0]+' where '+mark+' = \''+value+'\';'
			else:
				exit()
		try:
			cursor.execute(search_sql)
			sql_value = cursor.fetchall()
		except:
			pass
			sql_value = None
		if sql_value:
			print '---------------------------------'*2
			print 'From:	'+i[0]+'\r\n'
			if len(sql_value) > 1:
				for z in sql_value:
					for x in z:
						try:
							print x,
						except:
							pass
					print '\r'
#				print '\r\n'
			else:
				for z in sql_value:
					for x in z:
						try:
							print x,
						except:
							pass
				print '\r\n'
				
	endtime = datetime.datetime.now()
	print 'Use time:	'+str((endtime - starttime).seconds)+'	S'
		

	
	
if __name__ == "__main__":
	if len(sys.argv) !=4:
		usage()
		exit()
	mark = sys.argv[1]
	like = sys.argv[2]

	if 'nt' in os.name:
		value = unicode(sys.argv[3],'GBK')
	else:
		value = sys.argv[3]
	usage()
	search(mark,value,like)

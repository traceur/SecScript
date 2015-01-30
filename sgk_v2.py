#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#Code : Qiaoy<TraceurQ@gmail.com>

'''
mysql 社工库查询脚本
'''

import MySQLdb,sys,datetime
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

try:
    conn = MySQLdb.connect(host='localhost',user='root',passwd='XXX',db='shegong',charset='utf8')
except Exception, e:
    print e
    sys.exit()

	
def usage():
	print 'python sgk.py [name/email/QQNum/realname/tel/ctfid/passwd] value'

def search(mark,value):
	starttime = datetime.datetime.now()
	cursor = conn.cursor()
	list_table = 'select table_name from information_schema.tables where table_schema=\'shegong\''
	cursor.execute(list_table)
	sql_tables = cursor.fetchall()
	for i in sql_tables:
		search_sql = 'select * from '+i[0]+' where '+mark+' like \'%'+value+'%\';'
		try:
			cursor.execute(search_sql)
			sql_value = cursor.fetchall()
		except:
			pass
			sql_value = None
		if sql_value:
			print '-----------------------'
			print 'From:	'+i[0]+'\r\n'
			if len(sql_value) > 1:
				for z in sql_value:
					for x in z:
						try:
							print x,
						except:
							pass
					print '\r\n'
				print '\r\n'
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
	if len(sys.argv) !=3:
		usage()
		exit()
	mark = sys.argv[1]
	value = sys.argv[2]
	search(mark,value)

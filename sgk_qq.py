#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#Code : Qiaoy<TraceurQ@gmail.com>

'''
QQ群 关系查询脚本
'''

import MySQLdb,sys,datetime

try:
    conn = MySQLdb.connect(host='localhost',user='root',passwd='xxxxxx',db='qun',charset='utf8')
except Exception, e:
    print e
    sys.exit()

	
def usage():
	print 'python qqsgk.py [QQNum/QunNum] key'

def search(value,op):
	starttime = datetime.datetime.now()
	cursor = conn.cursor()
	list_qun_table = 'select table_name from information_schema.tables Where table_name LIKE \'shegong_qun_group%\''
	list_group_table = 'select table_name from information_schema.tables Where table_name LIKE \'shegong_qun_qunlist%\''
	cursor.execute(list_qun_table)
	sql_group = cursor.fetchall()
	cursor.execute(list_group_table)
	sql_qunlst = cursor.fetchall()
	if op == 'QQNum':
		print 'QQNum		Nick		QunNum		QunTitle		QunInfo'
		for i in sql_group:
			search_sql = 'select QQNum,Nick,QunNum from '+i[0]+' where QQNum = '+value
			cursor.execute(search_sql)
			sql_value = cursor.fetchall()
			if sql_value:
				for j in sql_value:
					for k in sql_qunlst:
						search_quninfo = 'select Title,QunText from '+k[0]+' where QunNum = '+str(j[2])
						cursor.execute(search_quninfo)
						quninfo_value = cursor.fetchall()
						if search_quninfo:
							for l in quninfo_value:
								print str(j[0])+'	'+j[1]+'	'+str(j[2])+'	'+l[0]+'	'+l[1],
								print '\r'

	elif op == 'QunNum':
		print 'QQNum		Nick		QunNum'
		for i in sql_group:
			search_sql = 'select QQNum,Nick,QunNum from '+i[0]+' where QunNum = '+value
			cursor.execute(search_sql)
			sql_value = cursor.fetchall()
			if sql_value:
				for j in sql_value:
					print str(j[0])+'	'+j[1]+'	'+str(j[2]),
					print '\r'
		
		
	endtime = datetime.datetime.now()
	print 'Use time:	'+str((endtime - starttime).seconds)+'	S'
		

	
	
if __name__ == "__main__":
	if len(sys.argv) !=3:
		usage()
		exit()
	value = sys.argv[2]
	op = sys.argv[1]
	search(value,op)

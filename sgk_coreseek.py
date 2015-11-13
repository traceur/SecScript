# -*- coding: UTF-8 -*- 
from sphinxapi import *
import sys, time,json
import MySQLdb

try:
    conn = MySQLdb.connect(host='localhost',user='root',passwd='',charset='utf8')
except Exception, e:
    print e
    sys.exit()


q = ''  #value
mode = SPH_MATCH_ALL
host = '192.168.1.219'  #sphinx host
port = 9000     #sphinx port
index = '*'
filtercol = 'aid'   #sql_query = SELECT `id`, 2 AS aid, `name`,`email` FROM shegong_xxx
filtervals = []
sortby = ''
groupby = ''
groupsort = '@group desc'
limit = 200

tables = ['']   #All tables
# do query
cl = SphinxClient()
cl.SetServer ( host, port )
cl.SetWeights ( [100, 1] )
cl.SetMatchMode ( mode )
res = cl.Query ( q, index )

if not res:
	print 'query failed: %s' % cl.GetLastError()
	sys.exit(1)

if cl.GetLastWarning():
	print 'WARNING: %s\n' % cl.GetLastWarning()

print 'Query \'%s\' retrieved %d of %d matches in %s sec' % (q, res['total'], res['total_found'], res['time'])
print 'Query stats:'

if res.has_key('words'):
	for info in res['words']:
		print '\t\'%s\' found %d times in %d documents' % (info['word'], info['hits'], info['docs'])

if res.has_key('matches'):
	n = 1
	print '\nValue:\n\n'
	for match in res['matches']:
		attrsdump = ''
		for attr in res['attrs']:
			attrname = attr[0]
			attrtype = attr[1]
			value = match['attrs'][attrname]
			if attrtype==SPH_ATTR_TIMESTAMP:
				value = time.strftime ( '%Y-%m-%d %H:%M:%S', time.localtime(value) )
			attrsdump = '%s, %s=%s' % ( attrsdump, attrname, value )
		n += 1
#		print '%d. doc_id=%s, weight=%d%s' % (n, match['id'], match['weight'], attrsdump)
		sql ="select * from shegong.%s where id = '%s';"%(tables[value - 1],match['id'])
		cursor = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
#		cursor = conn.cursor()
		cursor.execute(sql)
		sql_value = cursor.fetchall()
		for i in sql_value:
			print tables[value - 1].replace('shegong_','')+':'
			print json.dumps(i, encoding="UTF-8", ensure_ascii=False)
			print '-'*20

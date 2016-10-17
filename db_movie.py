#!/usr/bin/env python
#Qiaoy<traceurq@gmail.com>
#date:2015.05.20
#coding = utf-8
'''
豆瓣电影备份

依赖pyquery库

sudo pip install pyquery
'''

import sys,urllib2,re
from pyquery import PyQuery as pq


if len(sys.argv) != 2:
	print '	python douban_movie.py name'
	sys.exit(1)
else:
	site_value = urllib2.urlopen('http://movie.douban.com/people/%s/collect'%sys.argv[1]).read()
	movie_number = re.findall('<h1>.*\((\d*)\).*</h1>',site_value)[0]

	for i in xrange(0,int(movie_number),15):
		site_url = pq('http://movie.douban.com/people/%s/collect?start=%s'%(sys.argv[1],i))

		for m in site_url('div').filter('.item'):
		    z = pq(m)
		    print z('em').text().encode('utf8')
		    print z('span').filter('.comment').text().encode('utf8')
		    print '======================'

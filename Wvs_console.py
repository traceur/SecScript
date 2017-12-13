#!/usr/bin/python
# coding: UTF-8
#coder:qiaoy
'''
wvs_console 批量扫描脚本
'''

import sys,os,time

urllist = r'd:\\urllist.txt'	#需扫描网站列表文件
savefolder = r'd:\\result\\'	#扫描结果保存路劲
wvs_console = r'F:\\"Program Files (x86)"\\Acunetix\\"Web Vulnerability Scanner 9.5"\\wvs_console.exe'	#wvs_console路径


def scan(url,folder):
	if 'http' in url:
		name = url.split('//')[1].replace('/','')
		url = url
	else:
		name = url.replace('\n','')
		url = 'http://'+url
	name = name.replace('\n','')
	url = url.replace('\n','')
	if name in os.listdir(folder):
		print '%s has scaned'%name
	else:
#		os.system('%s'%wvs_console)
		os.system('%s /Scan %s /Profile ws_default /saveFolder %s%s --GetFirstOnly=false --FetchSubdirs=true --RestrictToBaseFolder=true --ForceFetchDirindex=true --SubmitForms=true --RobotsTxt=true --CaseInsensitivePaths=false --UseCSA=true --UseAcuSensor=true --EnablePortScanning=false --UseSensorDataFromCrawl=revalidate --ScanningMode=Heuristic --TestWebAppsOnAllDirs=false --ManipHTTPHeaders=true'%(wvs_console,url,folder,name))



if __name__ == '__main__':
	if not os.path.exists(urllist):
		print r'需扫描的网站文件不存在'
	if os.path.exists(savefolder) == False:
		os.mkdir(savefolder)
	for i in open(urllist):
		scan(i,savefolder)

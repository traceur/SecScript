#coding:utf-8

'''
Mysql多数据库自动同步到ES，通过Logstash的jdbc配置文件去推，配置文件放置在./config/test/目录下
事件日志实时生成到本目录下的cmd.log文件
'''

import subprocess
import sys,psutil
import time,os
def record_cmd(arg):
    os.chdir('F:\\logstash-5.6.1')
    proc = subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    while 1:
        logfile = open('cmd.log', 'ab')
        logfile.write('\r\n'.encode())
        out = proc.stdout.readline()
        if out == b'':
            break
        yield logfile.write(out.rstrip())
        logfile.close()

def execute_cmd(arg):
    for i in record_cmd(arg):
        pass

def check_logstash_state():
    logstash_state = 0
    pids = psutil.pids()
    for pid in pids:
        p = psutil.Process(pid)
        if p.name() == 'java.exe':
            logstash_state = 1
    return logstash_state

if __name__ == '__main__':
    data_name = []
    for i in open('F:\\data1.csv', 'r'):
        data_name.append(i.replace('\n',''))

    while True:
        if check_logstash_state():
            time.sleep(60)
        else:
            data_name_now = data_name.pop()
            execute_cmd('bash ./bin/logstash -f ./config/test/%s.conf'%data_name_now)
        if len(data_name) == 0:
            break

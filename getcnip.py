#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import urllib

def getcnip():
    # 将要匹配的字符串用正则表达式表示并编译为pattern实例
    regularIpv4 = re.compile(r'apnic\|CN\|ipv4\|(.*)\|(.*)\|(.*)\|allocated')

    # 新建ips.txt文件并打开
    with open("ips.txt", 'w') as f:     
        # 逐行读取网址中的内容到i
        for i in urllib.urlopen("http://ftp.apnic.net/apnic/stats/apnic/delegated-apnic-latest"):  
            # 判断是否匹配，如果匹配继续往下执行，否则匹配下一行
            if regularIpv4.findall(i):
                """
                sub(repl, string[, count]): 
                
                功能:
                    使用repl替换string中每一个匹配的子串后返回替换后的字符串。 
                当repl是一个方法时，这个方法应当只接受一个参数（Match对象, 并返回一个字符串用于替换(返回的字符串中不能再引用分组)。 
                count用于指定最多替换次数, 不指定时全部替换, 缺省值为1。 

                参考:
                    http://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html
                """
                result = regularIpv4.sub(func, i)
                # print result
                # 将结果写入到ips.txt文件中 
                f.write(result)

def func(m):
    """
    功能: sub函数第一个参数 repl, 用来返回一个字符串替换sub函数中的第二个参数 string

    apnic|CN|ipv4|27.112.0.0|16384|20100702|allocated

    m.group(1) 中存放的是 ip 地址 如上面的 27.112.0.0
    m.group(2) 中存放的是 待处理的掩码数 如上面的 16384
    """
    return m.group(1) + "/" + str(32 - testlog2(m.group(2)))

def testlog2(num):
    """
    功能: 已知 b 且 2^x=b, 求其中的x 
    具体实现请参考: http://blog.csdn.net/hackbuteer1/article/details/6681157
    """

    num = int(num)
    x = 0
    while num > 1:
        num >>= 1
        x += 1
    return x
 
if __name__ == '__main__':
    getcnip()
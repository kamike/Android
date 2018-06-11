#!/usr/bin/env python
# -*- coding:utf8 -*-
from xml.dom import minidom
from xml.dom.minidom import parse
import xml.etree.ElementTree as ET
import time

import operator as op

# 筛选出两个资源文件，有哪些改动


xmlZh = parse("C:/Users/wangtao/Desktop/temp/strings.xml")

coll = xmlZh.documentElement
string = coll.getElementsByTagName("string")
dirctOne = {}
for s in string:
    key = s.getAttribute("name")
    value = s.childNodes[0].data
    dirctOne[key] = value

# for l in dirctZh:
#     print(dirctZh[l])

xmlTow = parse("C:/Users/wangtao/Desktop/temp/strings22.xml")
collTow = xmlTow.documentElement
stringTow = collTow.getElementsByTagName("string")
dirctTow = {}
for s in stringTow:
    key = s.getAttribute("name")
    node = s.childNodes
    if len(node):

        value = node[0].data
        dirctTow[key] = value
    else:
        print(key + "的值是空的===")

# 开始比较

differentDir = {}

for keyOne in dirctOne:

    currentStr = dirctOne[keyOne]
    # print("当前比较的字符串："+currentStr)
    hashEn = 1;

    # if not keyOne in dirctTow.keys():
    if not op.eq(currentStr, dirctTow[keyOne]):
        print("查找到英文没有的值了：" + currentStr)
        differentDir[keyOne] = dirctTow[keyOne]

print("找到多少个不同的：" + str(len(differentDir)))
print(differentDir)
# 打印结果
for c in differentDir:
    print("找出了不同:" + str(c) + "," + differentDir.get(c))

out_file = open("C:/Users/wangtao/Desktop/temp/strings-different.xml", 'w+')

out_file.write("<resources>\n")
for key in differentDir:
    out_file.write("<string name=\"" + key + "\">" + differentDir.get(key) + "</string>\n")
out_file.write("</resources>")

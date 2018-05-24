#!/usr/bin/env python
# -*- coding:utf8 -*-
from xml.dom import minidom
from xml.dom.minidom import parse
import xml.etree.ElementTree as ET
import time

xmlZh = parse("C:/Users/wangtao/Desktop/temp/strings.xml")

coll = xmlZh.documentElement
string = coll.getElementsByTagName("string")
dirctZh = {}
for s in string:
    key = s.getAttribute("name")
    value = s.childNodes[0].data
    dirctZh[key] = value

# for l in dirctZh:
#     print(dirctZh[l])

xmlEn = parse("C:/Users/wangtao/Desktop/temp/strings-en.xml")
collEn = xmlEn.documentElement
stringEn = collEn.getElementsByTagName("string")
dirctEn = {}
for s in stringEn:
    key = s.getAttribute("name")
    node = s.childNodes
    if len(node):
        value = node[0].data
        dirctEn[key] = value
    else:
        print(key + "的值是空的===")

# 开始比较

differentDir = {}

for keyZh in dirctZh:
    currentStr = dirctZh[keyZh]
    # print("当前比较的字符串："+currentStr)
    hashEn = 1;

    if not keyZh in dirctEn.keys():
        print("查找到英文没有的值了：" + currentStr)
        differentDir[keyZh] = currentStr

print("找到多少个不同的：" + str(len(differentDir)))
print(differentDir)
# 打印结果
for c in differentDir:
    print("找出了不同:" + str(c) + "," + differentDir.get(c))

out_file = open("C:/Users/wangtao/Desktop/temp/strings-res.xml", 'w+')

out_file.write("<resources>\n")
for key in differentDir:
    out_file.write("<string name=\"" + key + "\">" + differentDir.get(key) + "</string>\n")
out_file.write("</resources>")


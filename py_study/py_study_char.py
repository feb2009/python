# -*- coding:UTF-8 -*-

# 文件的读写
import re
import os
import csv
import mmap
import xlrd
# context = '''\nhello world'''
# f = open ('hello.txt','a') # 打开文件
# f.write(context) #写入文件
k = open ('hello.txt')
context1 = k.read(5)
print (context1)
print (k.tell())
k.close()
k = open ('hello.txt')
context1 = k.read(10)
print (context1)
print (k.tell())
k.close()  #关闭文件




# # 一次多行
# f = open ("hello.txt")
# lines = f.readlines()
# for line in lines:
#     print(line)
# f.close()



# # 一次一行
# f = open ("hello.txt")
# while True:
#      line = f.readline()
#      if line:
#          print (line)
#      else:
#          break
# f.close()



#正则表达式
# ^ 正则表达式开始字符 $ 正则表达式的结束字符 \w 匹配字母、数字、下划线 \W \w 匹配不是字母、数字、下划线
# \s 匹配空白字符 \S 匹配不是空白的字符 \d 匹配数字 \D 匹配非数字的字符
# \b 匹配单词的开始和结束 \B 匹配不是单词开始和结束的位置 .(点） 匹配任意字符、包括汉字 （）对正则表达式进行分组，一对圆括号表示一组
# [m] 匹配单个字符串 [m|m2...n] 匹配多个字符串 [m-n] 匹配m到n区间内的数字和字母 [^m]匹配除m以外的字符串
# *匹配零次或多次 + 匹配一次或多次 ? 匹配一次或零次 {m} 重复m次 {m,n}重复m到n次，其中n可以省略，表示m到任意次
#


# p = re.compile(r"(abc)\1")
# m = p.match("abcabcabc")

# print (m.group(0))
# print (m.group(1))
# print (m.group())
# p = re.compile(r"(?P<one>abc)(?P=one)")
# m = p.search("abcabcabc")
# print (m.group("one"))
# print (m.groupdict().keys())
# print (m.groupdict().values())
# print (m.re.pattern)
# #compile() 预编译
# s = "1abc23def45"
# p = re.compile(r"\d+")
# print (p.findall(s))
# print (p.pattern)


# tel1 = "0791-1234567"
# print (re.findall(r"\d{3}-\d{8}|\d{4}-\d{7}", tel1))
# tel2 = "010-12345678"
# print (re.findall(r"\d{3}-\d{8}|\d{4}-\d{7}", tel2))
# tel3 = "(010)-12345678"
# print (re.findall(r"[\(-]?\d{3}[\)-]?[\)-]?\d{8}|[\(-]?\d{4}[\)-]?[\)-]?\d{7}", tel3))


# s = "HELLO WORLD"
# print (re.findall(r"^hello",s))
# print (re.findall(r"^hello",s,re.I))
# print (re.findall("WORLD$",s))
# print (re.findall(r"world$",s,re.I))
# print (re.findall(r"\b\w+\b",s))
# #re.sub
# s = "hello world"
# print (re.sub("hello","hi",s,re.I))
# print (re.sub("hello","hi",s[-4:]))
# print (re.sub("world","china",s[-5:]))
#re.subn
# s = "你好 WORLD2"
# print ("匹配字母数字：" + re.sub(r"\w", "hi", s))
# print ("替换字母数字次数：" + str(re.subn(r"\w","hi", s) [1]))
# print ("匹配非字母数字的字符：" + re.sub(r"\W","hi",s))
# print ("替换非字母数字次数：" + str(re.subn(r"\W","hi", s) [1]))
# print ("匹配空格字符：" + re.sub(r"\s","*",s))
# print ("替换空格字符次数：" + str(re.subn(r"\s","*",s)[1]))
# print ("匹配非空格字符：" + re.sub(r"\S","hi",s))
# print ("替换非空格字符次数：" + str(re.subn(r"\S","hi",s)[1]))
# print ("匹配数字：" + re.sub(r"\d","2.0",s))
# print ("替换数字次数：" + str(re.subn(r"\d","2.0",s)[1]))
# print ("匹配非数字：" + re.sub(r"\D","2.0",s))
# print ("替换非数字次数：" + str(re.subn(r"\D","2.0",s)[1]))
# print ("匹配任意字符：" + re.sub(r".","hi",s))
# print ("替换任意字符次数：" + str(re.subn(r".","hi",s)[1]))


#字符串与日期的转换
#strftime()
# import time,datetime
# a = time.strftime("%Y-%m-%d %X",time.localtime())
# print (a)
#
# t = time.strptime("2016-06-06 16","%Y-%m-%d %H")
# print (t)
#
# y,m,d,h= t[0:4]
# print (datetime.datetime(y,m,d,h))


#字符串的替换

# sentence = "this is a apple."
# print (sentence.find("a"))
# sentence = "this is a apple."
# print (sentence.rfind("a"))

#replace (old, new[, max])
# sentence = "hello word, hello china"
# print (sentence.replace("hello","hi"))
# print (sentence.replace("hello","hi",1))
# print (sentence.replace("abc","hi",1))



#字符串反转
# def reverse(s):
#     out = ""
#     li = list(s)
#     for i in range(len(li),0,-1):
#         out = out + "".join(li[i-1])
#     return out
# print (reverse("hello"))



#截取多个子串，可以使用函数split()实现
# sentence = "bob said: 1, 2, 3, 4"
# print ("使用空格取子串：", sentence.split())
# print ("使用逗号取子串：", sentence.split(","))
# print ("使用两个逗号取子串：", sentence.split(",",2))
# str1 = "a"
# print (id(str1))
# print (id(str1 + "b"))
#字符串比较
# str1 = 1
# str2 = "1"
# if str1 == str2:
#     print ("相同")
# else:
#     print ("不相同")
# if str(str1) == str2:
#     print ("相同")
# else:
#     print ("不相同")
#
# word = "hello world"
# print ("hello" == word[0:5])
# print (word.startswith("hello"))
# print (word.endswith("ld"))
# print (word.endswith("ld",6,10))
# print (word.endswith("ld",6,len(word)))

# word = "world"
# print (word[4])
# str1 = "hello world"
#
# aa = str1[::3] v
# print (aa)
# print (str1[0:3])
# print (str1[::3])
# print (str1[1::2])



#python 的制表符只占一个字符
# path = "hello \t world \n"
# print (path)
# print (len(path))
# path = r"hello\tworld\n" #忽略转义符的作用
# print (path)
# print (len(path))

#strip() 去掉转义字符
# word = "\thello world\thello hello"
# print ("直接输出：", word)
# print ("strip()后输出：", word.strip())
# print ("lstrip()后输出：", word.lstrip())
# print ("rstrip()后输出：", word.rstrip())
# 连接字符串 +
# str1 = "hello "
# str2 = "world "
# str3 = "hello "
# str4 = "china "
# result = str1 + str2 + str3
# result += str4
# print(result)
# #用加号连接稍显烦锁，PYTHON提供了函数JOIN（）连接字符串，JOIN()配合列表实现多个字符串的连接
# #使用JOIN
#
# strs = ["hello","world","hello","china"]
# result = " ".join(strs)
# print (result)
#
# #使用REDUCE函数实现实符串连接功能
# from functools import reduce
# import operator
# strs = ["hello ","world ","hello ","china "]
# result = reduce(operator.add, strs, " ")
# print (result)



# 字符串对齐函数
# word = "version 3.0"
# print (word.center(20)) #居中20个字符宽度
# print (word.center(20,"*"))
# print (word.ljust(0))
# print (word.ljust(20))
# print (word.__len__())
# print ("%30s" % word)
# 定义了一个匿名字典，该字典中的两个VALUES值分别对应字符串的%(version)s and %（num).1f
# print ("%(version)s: %(num).1f" %{"version":"version","num":2})

# str1 = "version"
# num = 1.0
# format = "%s" % str1
# print (format)
# format = "%s %d" %(str1,num)
# print (format)
#
# print ("浮点型数字： %f" % 1.25)  # 以浮点数格式打印
# print ("浮点型数字:  %.1f" % 1.25)  #精确到小数点后1位
# print ("浮点型数字:  %.2f" % 1.25)
#
# a=1
# print ("整型： %d%%" % 1.25)
# print ("大写16进制:  %X" % 1234666666)
# print ("8进制:  %o" % 1234666666)






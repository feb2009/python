# -*- coding:UTF-8 -*-
import io
import sys
import difflib
file1 = open("hello.txt","r")
file2 = open("hi.txt","r")
src = file1.read()
dst = file2.read()
print (src)
print (dst)
s = difflib.SequenceMatcher( lambda x:x == "",src,dst)
for tag,i1,i2,j1,j2 in s.get_opcodes():
    print ("%s src[%d:%d]=%s dst[%d:%d]=%s" , (tag,i1,i2,src[i1:i2],j1,j2,dst[j1:j2]))

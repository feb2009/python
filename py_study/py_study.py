# -*- coding:UTF-8 -*-
import math
import copy
import sys
# print(set(sys.modules.keys()))
# print(set(sys.modules.values()))
# print(sys.modules["os"])


#PYTHON2版本和PYTHON3版本运行结果不一样
# d=sys.modules.copy()
# import copy,string
# print (zip(set(sys.modules) - set(d)))


# dict={"a":"apple","b":{"g":"grape","o":"orange"}}
# dict2=copy.deepcopy(dict) #浅COPY 会改变原字典数据
# dict3=copy.copy(dict) #深COPY 不会改变原字典数据
# dict2["b"]["g"]="orange"
# print(dict2)
# print(dict)
# dict3["b"]["g"]="orange"
# print(dict3)
# print(dict)

# dict={}
# dict.setdefault("a")
# print(dict)
# dict["a"]="apple"
# dict.setdefault("a","none")
# print(dict)
# dict["a"]="none"
# print(dict)
# dict1={"b1":"apple1","a1":"banana","o1":"grape","k1":"orange"}
# #字典值 排序
# print(sorted(dict1.items(),key=lambda d:d[1]))
# print(sorted(dict1.items(),key=lambda d:d[0]))

# #字典的UPDATE
# dict={"a":"apple","b":"banana"}
# print(dict)
# dict1={"g":"grape","o":"orange"}
# dict.update(dict1)
# print(dict)

# #字典的方法
# dict={"a":"apple","b":"banana","g":"grape","o":"orange"}
# dict1={"a1":"apple1","b1":"banana","g1":"grape","o1":"orange"}
# print(dict.keys())
# print(dict.values())
# #用FOR IN 将DCIT1中的值逐个添加至DICT中
#
# for k in dict1:
#     print(k)
#     dict[k]=dict1[k]
#     print(dict)
# print (dict)
# # a=input("请输入：")
# # print(dict.get(a,"china"))



#混合型字典，元组，列表甚至字黄都可以作为字典的value值，
#格式：dict={"key1":(tuple),"key2":(list),"key3":{dict}...}
# dict={"a":("apple","china"),"bo":{"b":"banana","o":"orange"},"g":["grape","grapefruit"]}
# print(dict["a"])
# print(dict["a"][0])
# print(dict["bo"])
# print(dict["bo"]["o"])
# print(dict["g"])
# print(dict["g"][1])


# #素数
# list_num=[]
# for i in range(1,100000):
#     for num in range(2,int(math.sqrt(i))+1):
#         if i % num ==0 and i != num:
#             break
#         elif i % num !=0 and num==int(math.sqrt(i)):
#             list_num.append(i)
#             print(i,end=" ")
# # print(list_num)


#字典遍历
# dict={"a":"apple","b":"banana","g":"grape","o":"orange"}
# for k in dict:
#     print("dict[%s]="%k,dict[k])
#
# dict={1:"apple",2:"banana",3:"grape",4:"orange"}
# for k in dict:
#     print("dict[%s]="%k,dict[k])  #,end="")
#items()返回一个由若干元组组成的列表
# dict={"a":"apple","b":"banana","g":"grape","o":"orange"}
# print(dict.items())
# for(k,v) in dict.items():
#     print("dict[%s]:"%k,v,v,end=" ")
#     print(v)

# #字典的访问 赋值
# #字典是无序的，因此字典没有append()，remove()等方法，如果需要向字典中插入新的元素，可以调用setdefault
# dict={"a":"apple","b":"banana","g":"grape","o":"orange"}
# dict["w"]="watermelon"
# print(dict)
# del(dict["a"])
# print(dict)
# dict.clear()
# print(dict)


# #字典的创建 字典的键区分大小写，也可以用数字做索引
# dict={"a":"apple","b":"banana","g":"grape","o":"orange"}
# dict1={1:"apple",2:"banana",3:"grape",4:"orange"}
# print(dict)
# print(dict1)
# print(dict["a"])
# print(dict1[2])
# print("%s,%(a)s,%(b)s"%{"a":"apple","b":"banana"})
#
# ab=dict1[2]
# print(ab)
#列表的查找、排序、反转

# list1 = ["banana","apple","orange","grape"]
# list1.sort() #正序
# print(list1)
# list1.reverse() #反序
# print(list1)
# print(list1.index("apple"))
# print(list1.pop())


#列表的使用print(list1)
# list1=["apple","banana"]
# list2=["grape","orange"]
# list1.extend(list2)
# print (list1)
# list3=["watermelon"]
# list1=list1+list3
# print (list1)
# list1=list1+["grapefruit"]
# print (list1)
# list1=list1*2
# print(list1)
# list1=["apple","banana"]*2
# print(list1)
#列表数据可以增，删，改
# 元组格式用（） 列表用[] 字典用{}
# list=["apple","banana","grape","orange"]
# print(list)
# print(list[2])
# print(list[1:3])
# list.append("watermelon") #追加
# list.insert(3,"grapefruit") #插入
# print(list)
# list.remove("grape") #移除
# print(list)
# list.remove("apple")
# print(list.pop())  #POP调用最后一个元素
# print(list)


# list2=[["apple","banana"],["grape","orange"],["watermelon",],["grapefruit",]]
# for i in range(len(list2)):
#     print("list[%d]:"%i,end=" ",) #PY3.0默认换行，不换行要end=""
#     for j in range(len(list2[i])):
#         print(list2[i][j],end=" ",)
#     print()
# list = ["apple","A"]
# print(list[0])
# list.remove("apple")
# print(list[0])

#元组数据不可以添加，删除
# tuple=(("apple","banana"),("grape","orange"),("watermelon",),("grapefruit",))
# for i in tuple:
#     print (i)
#     for j in i:
#         print(j)
# print()
#
# for leni in range(len(tuple)):
#     print ("tuple[%d] :"%leni,end="")
#     for lenj in range(len(tuple[leni])):
#         print (tuple[leni][lenj],end="")
#     print()


# #打包
# tuple=("apple","banana","grape","orange")
# #解包
# print(len(tuple))
# a,b,c,d=tuple
# print(a,'+',b,c,d)


# tuple1 = ("apple")
# print(tuple1[0])
# tuple1[0]="a"


# print(type(tuple1))
# tuple = ("apple",) #创建唯一元素的元组，需要在元素的后面加一个逗号
# print(tuple[0])
# print(type(tuple))
# tuple = ("apple","banana","grape","orange") #创建唯一元素的元组，需要在元素的后面加一个逗号
# #print(tuple[1:4])
# tuple3=tuple[1: 3]
# tuple4=tuple[0: -2]
# tuple5=tuple[2: -1]
# print(tuple3)
# print(tuple4)
# print(tuple5)
# 元组还可以由其他元组组成，例如：二元元组可以表示为：
# tuple=(('t1','t2'),('t3','t4'))
# fruit1=("apple","banana")
# fruit2=("grape","orange")
# tuple1=(fruit1,fruit2)
# print(tuple1)
# print(tuple1[0][0])
# print(tuple1[0][1])
# print(tuple1[1][0])
# print(tuple1[1][1])





# 冒泡法
# def bubblesort(numbers):
# for j in range(len(numbers) - 1, -1, -1):
#         print(j)
#         for i in range(j):
#             if numbers[i]<numbers[i+1]:
#                 numbers[i],numbers[i+1]=numbers[i+1],numbers[i]
#                 print(numbers)
# def main():
#     numbers = [23,12,9,15,6,10,20,100,1]
#     bubblesort(numbers)
# if __name__=='__main__':
#     main()



#continue 用法
# x=0
# for i in [1,2,3,4,5]:
#     if x == i:
#  #     print(x)
#       continue
#     x = x + i
#     print(x)
# print("x values:",x)


#how to use break
# x=int(input("input x values:"))
# y=0
# for y in range(0,100):
#     if(x == y):
#         print("find number:",x)
#         break
# else:
#     print("not find number")


# i= range(-2,5)
# print(i)
#
# for x in i:
#     if x>0:
#         print("正数：",x)
#     elif x == 0:
#         print("零：",x)
#     else :
#         print("负数：",x)
# else:
#     print("循环结束！")






# while 循环
# x=float(input("input x value:"))
# i=0
# while(x!=0):
#     if(x>0):
#         x=x-1
#     else:
#         x=x+1
#     i=i+1
#     print("第%d次循环：" %(i),x)
# else:
#     print("x等于0:",x)




# numbers = input("input some number,use ','rupt:").split(",")
# print(numbers)
# print(len(numbers))
# x=0
# while x<len(numbers):
#     print (numbers[x])
#     x=x+1



#SWITCH的替代方案
# import __future__
# #from __future__ import division
# x=5
# y=2
# operator=input("input operator( + - * /)")
# result={
#     "+":x + y,
#     "-":x - y,
#     "*":x * y,
#     "/":x / y,
# }
# print(result.get(operator))

# a = input("a:")
# print(id(a))
# a = int (a)
# print(id(a))
# b = input("b:")
# b = int (b)
# if(a > b):
#     print(a,">",b)
# elif(a < b):
#     print(a,"<",b)
# else:
#     print(a,"=",b)



#字符串 __doc__属性
# class hello:
#     '''hello class'''
#     def printhello():
#         '''print hello world'''
#         print("hello world")
# print(hello.__doc__)
# print(hello.printhello.__doc__)
#
# print(2**38)

#数据类型
# i = 1
# print(id(i))
# print(type(i))
# i = 2
# print(id(i))
# print(type(i))
#
# type_c=1+8j
# print(type(type_c))
#
# import global_var      #全局变量文件
# def fun():
#     print(global_var._a)
#     print(global_var._b)
# fun()
# #局部变量
# def fun():
#     local=1
#     print(local)


#全局变量
# _a=1
# _b=2
# def add():
# #    global _a
#     _a=3
#     return "_a + _b =",_a + _b
# def sub():
# #    global _b
#     _b=3
#     return "_a - _b =", _a - _b
# print(add())
# print(sub())




# 换行代码格式
# sql="select id,name "\
#     " from dept"\
#     " where  name='test'"
# print (sql)
#
# a=(1,2,3)
# (x,y,z)=a
# print (a)
# print(x,y,z)
# print(x)
# print(y)
# print(z)


# import sys
# print(sys.path)
# print(sys.argv)
# print(sys.copyright)
#
# 定义函数
#  import random
# def compareNum(num1,num2):
#     if(num1>num2):
#         return "1大于2"
#     elif(num1<num2):
#         return "1小于2"
#     else:
#         return "相等"
# num1=random.randrange(1,100,1)
# num2=random.randrange(1,100,1)
# print("num1 =",num1)
# print("num2 =",num2)
# print(compareNum(num1,num2))
#



#
# print (1+9)
# print ('hello world')
# x=1
# while x<11:
#     print (x)
#     x=x+1
#
# for i in range(10):
#     print (i)
#     if i==8:
#         break
#

# class Student:
#     __name=""
#     def __int__(self,name):
#         self.__name = name
#     def getName(self):
#         return self.__name
# if __name__ == "__main__":
#     student=Student("borphi")
#     print(student.getName())





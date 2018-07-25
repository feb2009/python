# -*- coding:UTF-8 -*-

#查看当前时间周几
import time
import datetime

def myweekday(date):
    weekdaydict = {0: '星期一',
                   1: '星期二',
                   2: '星期三',
                   3: '星期四',
                   4: '星期五',
                   5: '星期六',
                   6: '星期天'
                   }
    day = date.weekday()
    print(day)
    return weekdaydict[day]
print (myweekday(datetime.datetime.now()))



#generator 函数：生成器的作用是一次产生一个数据项，并把数据项输出，可以在FOR循环中遍历，每次返回一个数据项的特性
# yield与return关键字的返回值和执行原理不相同，yield生成值不会中止程序中执行
# def fund1(n):
#     for i in range(n):
#         yield i
#
# def fund2(n):
#     for i in range(n):
#         return i
# print(fund2(3))
# f = fund1(3)
# print (f)
# print (f.next())
# print (f.next())
# print (f.next())
# print (f.next())

# s = lambda x, y: x + y
# print (s('aa', 'bb'))
# for i in fund(3):
#     print(i)
# r = fund1(3)
# print (r())
# print (r.next())
# print (r.next())
# print (r.next())




#lambda 创建一个匿名函数，函数名未和标识符进行绑定，使用LAMBDA函数可以返回一些简单的运算结果
# lambda 格式：lambda 变量1，变量2……：表达式 只能用表达式，不能使用判断、循环等多重语句

# def func():
#     x=1
#     y=2
#     m=3
#     n=4
#     sum=lambda x,y:x+y
#     print(sum)
#     sub=lambda m,n:m-n
#     print(sub)
#     return sum(x,y) * sub(m,n)
# print(func())
# print(ascii(input()))




#函数的递归 在函数主体直接或间接调用自己，是一种程序设计，可以减少代码重复，递归过程分递推和回归
#每次调用递归都会复制函数中的所有变量，再执行递归，对程序性能会有一定影响，可以用其它方法进行改进
# from functools import reduce
# print("100!=",reduce(lambda x,y:x*y,range(1,100)))


# #计算阶乘
# def refunc(n):
#     i=1
#     if n>1:
#         i=n
#         n=n*refunc(n-1)
#     print ("%d!="%i,n)
#     return n
# print(refunc(100))

#函数的嵌套 尽量控制在三层以内

# def sum(a,b):
#     print(a+b)
#     return a+b
# def sub(a,b):
#     print (a-b)
#     return a-b
# def fun2():
#     x=1
#     y=2
#     m=3
#     n=4
#     return sum(x,y) *sub(m,n)
# print(fun2())

# 返回多个值
# def func(x,y,c):
#     l=[x,y,c]
#     l.reverse() # 倒排序
#     numbers=tuple(l)
#     a,b,c=tuple(l)
# #   return numbers
#     return a,b,c
# x,y,c=func(1,2,3)
# print(x,y,c)
# #多个return 是不推荐的语法，通过增加变量的方法，减少return语句
# # def fun1(x):
# #     if x> 0:
# #         return "x>0"
# #     elif x==0:
# #         return "x=0"
# #     else:return "x<0"
# # print(fun1(-1))
# def fun1(x):
#     if x> 0:
#         result = "x>0"
#     elif x==0:
#         result= "x=0"
#     else:result= "x<0"
#     return result
# print(fun1(-1))



# 传递可变参数 *
# def funs(*args):
#     print(args)
# funs(1,2,3)
#
# # 传递可变参数 **
# def search(*t,**d): # * 必须写在**前面，这是语法规定
#     keys=d.keys()
#     values=d.values()
#     print(keys)
#     print(values)
#     for arg in t:
#         for key in keys:
#             if arg == key:
#                 print('find:',d[key])
# search("one","three",one="1",two="2",three="3")


# 调用
# from __future__ import division
# def arithmetic(x=1,y=1,op="+"):
#
#     result={
#         "+":x+y,
#         "-":x-y,
#         "*":x*y,
#         "/":x/y
#     }
#     print(x," ",y," ",op)
#     return result.get(op)
# print(arithmetic(2,3,"+"))
# print(arithmetic(4,5))
# print(arithmetic(op="-",y=4,x=2))

# def arithmetic(args=[],op="+"):
#     x=args[0]
#     y=args[1]
#     result={
#         "+":x+y,
#         "-":x-y,
#         "*":x*y,
#         "/":x/y
#     }
#     print(x," ",y," ",op)
#     return result.get(op)
# print(arithmetic([1,2]))
#
# def append(args=[]):
#     if len(args) <=0: # 条件判断语句 如果列表args没有任何元素，则先置空，再添加元素
#         args=[]
#     args.append(0)
#     print (args)
# append()
# append([1])
# append()


# from pack1 import mypack1
# from pack2 import mypack2

# from pack1 import *
# from pack2 import *
# mypack1.fun()
# mypack2.fun()



#MAP()
# def power(x):
#     return x ** x
# print(map(power,range(1,10)))
# print(list(map(power,range(1,10))))
# def power2(x, y): return x ** y
# print(map(power2, range(1, 10), range(5, 1, -1)))
# print(list(map(power2, range(1, 3), range(5, 1, -1))))
#
# #REDUCE()
# from py_study_module_fun import sumxy
# print(reduce(sumxy,range(0,10)))
# print(reduce(sumxy,range(0,10),10))
# print(reduce(sumxy,range(0,0),10))
#
# def power2(x, y): return x ** y
#
# print(map(power2, range(1, 5), range(5, 1, -1)))
#
# print(list(map(power2, range(1, 5), range(5, 1, -1))))




# def funfilter(x):
#     if x > 0:
#         return x
# print(filter(funfilter,range(-9,10)))
# print(list(filter(funfilter,range(-9,10))))

#import py_study_module_fun

#print(__doc__)


# py_study_module_fun.fun()
# myclass=py_study_module_fun.MyClass()
# myclass.myFunc()
#
# from py_study_module_fun import fun
# fun()

# import py_study_module_fun
# print("count =",py_study_module_fun.fixfunloadnum())
# py_study_module_fun.count=10
# import py_study_module_fun
# print("count =",py_study_module_fun.count)
# print("count =",py_study_module_fun.fixfunloadnum())

# if py_study_module_fun.count>1:
#     py_study_module_fun.count=1
# else:
#     import py_study_module_fun
# print("count =",py_study_module_fun.count)
#
# if __name__=='__main__':
#     print("module作为主程序运行")
#     print(__name__)
# else:
#     print("被别一个模块调用")


# -*- coding:UTF-8 -*-
def fun():
    print("MyModule.fun()")

class MyClass:
    def myFunc(self):
        print ("mymodule.MyClass.myFun()")


count=1
def fixfunloadnum():
    global count
    count=count+1
    return count


if __name__=='__main__':
    print("module作为主程序运行")
    print(__name__)
else:
    print("被别一个模块调用")

def sumxy(x,y):
    return x+y

def power2(x,y):
    return x**y


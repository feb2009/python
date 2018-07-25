# -*- coding:UTF-8 -*-

def fun():
    print("pack.mymodule.func()")

if __name__=="__main__":
    print("mymodule 作为主程序运行")
else:
    print("mymodule 被其它程序调用")
#!/usr/bin/env python
# -*- coding:utf-8 -*-

r"""
    #@ 此处说明程序用途、用法、示例等

    #@ 此处说明程序正常运行，除Python自带模块外需要的第三方依赖模块情况
"""
import sys
import os
import platform


########################################################################
class ProgramInit:
    """程序初始化类"""

    # 初始化程序属性
    program_name = 'cmccbj.py'
    CodeStyle = 'IceStyle Ver1.0.9'
    CreateDate = 20170224
    Version = '1.0.0'
    Author = 'Chris A.I. Pi'
    RunEnv = '2.7.13'

    gvarERROR_001 = u'Error-001! Python版本不符合程序需求'

# ----------------------------------------------------------------------
    def __init__(self):
        """初始化方法"""

        self.m_env_check()

# ----------------------------------------------------------------------
    def m_env_check(self):
        """运行环境检查方法"""

        if int(self.RunEnv.split('.')[0]) != int(sys.version_info[0]):
            # 检查运行环境是否符合要求（RunEnv属性）
            print(self.gvarERROR_001)
            print('    Your Python version: {0}, program does not support!\n'
                  '    Supported version: Python [{1}.x], Recommend to use: {2}.'
                  .format(platform.python_version(), self.RunEnv.split('.')[0], self.RunEnv))
            quit(1)  # 模块引用

# ----------------------------------------------------------------------
    def m_argv_get(self):
        """获取运行参数"""

        # 获取参数个数、参数内容
        # 数据结构：
        #     [int(参数个数), list(参数内容)]
        re = [len(sys.argv)-1, sys.argv]
        
        return re


# 参数处理
class ArgvParse:
    """参数解析类"""
    argv_list = list()

# ----------------------------------------------------------------------
    def __init__(self):
        """初始化方法"""

        if len(sys.argv) - 1 == 0:
            return
        else:
            # 根据实际需求更改
            # 具体由该类的对应方法处理
            for i in range(1,len(sys.argv) - 1):
                self.argv_list.append(i)


# 程序主体部分
class main:
    def __init__(self):
        for i in ArgvParse.argv_list:
            with open(i, 'r')as f:
                for j in f.readlines():
                    if j[0] == '#':
                        continue
                    os.system(j + ' >> log/cmccbj.log')


# 程序启动部分
if __name__ == '__main__':
    varAttr = ProgramInit()
    varArgv =


# 风格示例(编写模块类或者引用使用的代码段可不完全遵从此风格，以便与理解为上）
r"""    <<<多行注释
(((建议详细阅读本段内容)))    <<<注释强调文字

#详细规范参考：http://blog.sina.com.cn/s/blog_4958182c0102vy0v.html    <<<单行注释

#@
    lambda x, y: x + y    <<<示例内容，正式发布时删除，以 @# 结尾
@#

#$STRING    <<<替换会被解释器执行的注释

pass #TODO STRING    <<<临时伪代码，仅说明替代代码功能

#代码宽度：80个字符

#缩进方式：4个空格

class Name(object):
    #$文档字符串

    #----------------------------------------------------------------------
    def __init__(self, p_para1, p_para2)：
    #$文档字符串

        pass

    #----------------------------------------------------------------------
    def m_name(self):
    #$文档字符串

        pass


class Other(object):
    #$文档字符串

    pass


#----------------------------------------------------------------------
def other(p_name):
    #$文档字符串

    def f_other(p_name):
        #$文档字符串

        pass



v_name = '私有变量'
G_NAME = '全局变量'
p_name = '类或函数的参数'
"""

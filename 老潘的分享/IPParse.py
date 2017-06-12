#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import print_function

r"""
    #@ 此处说明程序用途、用法、示例等

    #@ 此处说明程序正常运行，除Python自带模块外需要的第三方依赖模块情况
"""
import sys
import platform
import os


########################################################################
class ProgramInit:
    """程序初始化类"""

    # 初始化程序属性
    program_name = 'IPParse'
    CodeStyle = 'IceStyle Ver1.0.8'
    CreateDate = 20161111
    Version = '1.0.0'
    Author = 'Chris A.I. Pi'
    RunEnv = '2.7.10'

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


# 程序主体部分
class ProgramMain():
    ParseFile = sys.argv[0]

    def __init__(self):
        self.result = list()

    def start(self):
        if os.path.exists(self.ParseFile):
            self.of = open(self.ParseFile, 'r')
        else:
            print("Parse File not found!")
            exit(1)

        self.m_parsefile()

    def m_parsefile(self):
        for i in self.of.readlines():
            if len(i)==1:
                continue
            tmp = i[:-1].split(' ')
            tmp[0] = tmp[0].split(':')[-1]
            self.result.append(tmp[:4])

        self.m_output()

    def m_output(self):
        for i in range(len(self.result[0])):
            print(self.result[0][i], end='')
            print(self.m_space(len(self.result[0][i]), 9) + ":  ", end='')
            print(self.result[1][i])

    def m_space(self, funclen, totallen):
        return " "*(totallen - funclen)

    def __del___(self):
        self.of.close()



# 程序启动部分
if __name__ == '__main__':
    varAttr = ProgramInit()
    varMain = ProgramMain()
    varMain.ParseFile = sys.argv[1]
    varMain.start()


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
def f_other(p_name):
    #$文档字符串

    pass


v_name = '私有变量'
G_NAME = '全局变量'
p_name = '类或函数的参数'
"""

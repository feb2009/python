#!/usr/bin/env python
# -*- coding:utf-8 -*-

r"""
    #@ 此处说明程序用途、用法、示例等
    用于在指定文本文件中进行增删改查等操作
    用法示例：
    放到python的Lib库搜索路径，在程序里执行：
    import fileOPS
    fo = fileOPS.OpenFile(r'''SvnPWMGR\\test.txt''')
    fo.finder('[users]\n')
    #@ 此处说明程序正常运行，除Python自带模块外需要的第三方依赖模块情况
"""
import sys
import os
import platform


########################################################################
class ProgramInit:
    """程序初始化类"""

    # 初始化程序属性
    ProgramName = 'SvnPWMGR'
    CodeStyle = 'IceStyle Ver1.0.7'
    CreateDate = 20160607
    Version = '1.0.0'
    Author = 'Chris A.I. Pi'
    RunEnv = '2.7.10'

    gvarERROR_001 = u'Error-001! Python版本不符合程序需求'

    Para = sys.argv[:]

    # ----------------------------------------------------------------------
    def __init__(self):
        """初始化方法"""

        self.method_env_check()

    # ----------------------------------------------------------------------
    def method_env_check(self):
        """运行环境检查方法"""

        if int(self.RunEnv.split('.')[0]) != int(sys.version_info[0]):
            # 检查运行环境是否符合要求（RunEnv属性）
            print(self.gvarERROR_001)
            print('    Your Python version: {0}, program does not support!\n'
                  '    Supported version: Python [{1}.x], Recommend to use: {2}.'
                  .format(platform.python_version(), self.RunEnv.split('.')[0], self.RunEnv))
            quit(1)  # 模块引用


# 程序主体部分
class OpenFile:
    def __init__(self, filename):
        midfilename = os.path.split(os.path.normpath(filename))
        self.filename = os.path.join(midfilename[0], midfilename[1])
        print self.filename

    def read(self):
        with open(self.filename, 'r')as fileSock:
            return fileSock.readlines()

    def write(self, text_content):
        with open(self.filename, 'w')as fileSock:
            try:
                fileSock.writelines(text_content)
            except IOError:
                return 1
            return 0

    def change(self, row_num, new_str):
        with open(self.filename, 'r')as fileSockR:
            with open(self.filename, 'w')as fileSockW:
                try:
                    text_content = fileSockR.readlines()
                    text_content[row_num] = new_str
                    fileSockW.writelines(text_content)
                except IOError:
                    return 1
                return 0

    def delete(self, row_num):
        with open(self.filename, 'r')as fileSockR:
            with open(self.filename, 'w')as fileSockW:
                try:
                    text_content = fileSockR.readlines()
                    result_content = list()
                    for Num in range(len(text_content)):
                        if Num == row_num:
                            continue
                        result_content.append(text_content[Num])
                    fileSockW.writelines(result_content)
                except IOError:
                    return 1
                return 0

    def finder(self, find_content):
        text_content = self.read()
        return text_content.index(find_content)


# 程序启动部分
if __name__ == '__main__':
    # varAttr = ProgramInit()
    # varPara = varAttr.Para
    print 'Canot used to command line, only import!'

# 风格示例
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

class ClassName(object):
    #$文档字符串

    #----------------------------------------------------------------------
    def __init__(self)：
    #$文档字符串

        pass

    #----------------------------------------------------------------------
    def method_name(self):
    #$文档字符串
        pass


class ClassOther(object):
    #$文档字符串

    pass



#----------------------------------------------------------------------
def func_other(paraName):
    #$文档字符串

    pass


varName = '私有变量'
varNAME = '常量'
gvarNAME = '全局变量'
paraName = '类或函数的参数'
"""

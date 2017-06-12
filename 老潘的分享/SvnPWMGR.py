  #!/usr/bin/env python
# -*- coding:utf-8 -*-

r"""
    #@ 此处说明程序用途、用法、示例等
    用于在指定SVN的passwd文件中维护username和password
    Server:
    Python SvnPWMGR.py [PORT] [PATH/FILENAME]
    #@ 此处说明程序正常运行，除Python自带模块外需要的第三方依赖模块情况
"""
import sys
import os
import platform
import socket
import thread


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
class PortListen:
    """
    用于制作Telnet Server
    使用方法：
    class test(PortListen):
        # print TextInput
        def commParse(self):
            self.conn.send('Done' + self.ENTER)

    if __name__ == '__main__':
    p = test(PORT)
    p.run()
    """
    userList = list()
    login = False

    def __init__(self, ListenPort):
        """
        """
        # 单行换行
        self.sENTER = '\r\n'
        # 双行换行
        self.dENTER = '\r\n\n'
        # 获取文件名
        self.varFile = varPara[2]
        # 文件操作锁
        self.varFileLock = 0
        # 监听端口
        self.varPort = ListenPort
        # 初始化命令行提示符
        self.prompt = 'SPWM-' + ProgramInit.Version + ' >'
        # 初始化欢迎信息
        self.varWelcome = 'SVN user manager\r\n' \
                          'Version: ' + ProgramInit.Version + self.dENTER
    def run(self):
        """
        """
        while 1:
            # 通过循环+多线程实现多用户并发访问
            # 获取Socket
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # 绑定接口信息
            self.sock.bind(('', int(self.varPort)))
            # 设置并发数
            self.sock.listen(9)
            # while 1:
            # 柱塞式连接，获取连接套接字和客户端地址
            self.conn, self.addr = self.sock.accept()
            # 发送欢迎信息
            self.conn.send(self.varWelcome)
            # 开启线程处理用户访问
            thread.start_new_thread(self.OpenPort,())

    def OpenPort(self):
        while 1:
            # 通过循环保证登陆后能够进入提示符
            if self.login:
                # 判断是否已经登陆，True已经登陆，False未登录
                # 发送提示符
                self.conn.send(self.prompt)
                # 初始化命令存储
                self.command = ''
                while self.command.rfind('\n') <= -1:
                    # 通过截取最后一个字符，判断是否是换行符来识别是否输入完命令
                    # 获得输入内容
                    self.command += self.conn.recv(1024)
                if len(self.command.strip()) == 0:
                    # 过滤掉只有空格或回车的无效输入
                    continue
                # 调用命令解析
                self.Parse()
            else:
                # 调用登陆信息
                self.userLogin()

    def userLogin(self):
        # 初始化登陆用户变量
        self.loginUser = None
        while 1:
            # 循环到输入正确的登陆信息
            # 等待输入用户名
            self.conn.send('Username: ')
            username = ''
            while username.rfind('\n') <= -1:
                username += self.conn.recv(1024)
            # 格式化输入的信息
            username = username.strip()
            for user in self.userList:
                # 通过遍历文件中获取的用户名，来校验输入的用户名
                if username == user[0]:
                    # 判断用户名是否正确，True继续输入密码，False通过伪装完成本次登陆
                    # 等待输入密码
                    self.conn.send('Password: ')
                    password = ''
                    while password.rfind('\n') <= -1:
                        password += self.conn.recv(1024)
                    # 格式化输入的信息
                    password = password.strip()
                    if  password == user[1]:
                        # 校验密码，True更改状态，设置当前用户，False通过伪装完成本次登陆
                        self.login = True
                        self.loginUser = user[0]
                        return self.login
                    else:
                        # 密码错误
                        self.conn.send('Login failed!' + self.sENTER)
                        continue
                else:
                    continue
            # 用户名错误，通过如下伪装使无从判断是用户名还是密码错误，从而提高安全性
            self.conn.send('Password: ')
            password = ''
            while password.rfind('\n') <= -1:
                password += self.conn.recv(1024)
            self.conn.send('Login failed!' + self.sENTER)
            return self.login

    def Parse(self):
        """
        抽象方法，继承后重构
        用于描述具体的解析方法
        """
        pass

import string
class FileRead():
    """
    文件读取
    """
    def open(self, pathfile):
        #
        # 初始化用户文件
        self.varFile = pathfile
        # 生成激活用户列表
        self.createActiveUserList()

    def createActiveUserList(self):
        with open(self.varFile, 'r') as f:
            # 读取全部内容
            self.lines = f.readlines()
            # 初始化用户行判断变量
            isUser = False
            # 初始化激活用户列表
            self.activeUser = list()
            for i in self.lines:
                # 遍历所有行
                # 格式化行，去掉首尾空格
                line = i.strip()
                if line == '':
                    # 过滤空行
                    continue
                elif line[0] == '#':
                    # 过滤屏蔽行
                    continue

                elif line == '[users]':
                    # 寻找user段
                    isUser = True
                elif isUser == True:
                    # 进入用户行模式
                    if line[0] == '[':
                        # 退出用户行模式
                        isUser = False
                    else:
                        # 将用户行内容切割，用户名使用元素0，密码使用元素1，作为List元素添加到激活用户列表
                        self.activeUser.append([line.split(' = ')[0].strip(), line.split(' = ')[1].strip()])
        return self.activeUser

    def lsUser(self):
        # 列出激活用户的用户名，返回值类型List
        user = list()
        for i in self.activeUser:
            user.append(i[0])

        return user

class CommParse(FileRead):
    """
    命令查询类，继承了文件读取类
    """
    def CParse(self, Command, Sock):
        """
        """
        # 格式化命令体
        self.comm = Command.strip().split(' ')
        # 每个命令一个elif
        if self.comm[0] == 'quit':
            self.conn.send('Bye!')
            sys.exit(0)
        elif self.comm[0] == 'ls':    # 命令ls执行体
            return self.lsUser()
        else:   # 非命令执行体
            return []


class test(PortListen, CommParse):
    # 主函数，分别继承了端口监听和命令解析类
    def Parse(self):
        """
        重构PortListen类的Parse方法
        """
        # 命令结果，类型List，一行一个元素
        commandResult = self.CParse(self.command, self.sock)
        # 遍历命令解析后执行体返回的List，并发送给连接用户
        for item in commandResult:
            self.conn.send(item + self.sENTER)
        if len(commandResult) <0:
            self.conn.send('[ Execute Successful! ]' + self.dENTER)
        else:
            self.conn.send('Not found command: ' + self.command)


# 程序启动部分
if __name__ == '__main__':
    varAttr = ProgramInit()
    varPara = varAttr.Para
    # 初始化主函数
    p = test(varPara[1])
    # 调用FileRead类的open方法，生成用户List
    p.open(varPara[2])
    # 为登陆提供验证信息
    p.userList = p.activeUser
    # 启动程序
    p.run()



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
